<template>
  <div class="chat-container">
    <!-- Voice Input Component -->
    <VoiceInput 
      @voiceInput="handleVoiceInput" 
      :isLoading="isLoading"
    />
    
    <!-- Text Output Component -->
    <TextOutput 
      :text="textOutput" 
      v-if="!isLoading"
    />

    <!-- Loading Spinner -->
    <div v-else class="loading-spinner" aria-live="polite">
      Processing your audio, please wait...
    </div>

    <!-- Added Error Message Component -->
    <ErrorMessage 
      v-if="errorMessage" 
      :message="errorMessage" 
      @clearError="clearError"
    />

    <!-- Added History Toggle Button -->
    <button 
      class="history-toggle" 
      @click="toggleHistory" 
      aria-label="Toggle chat history"
    >
      {{ showHistory ? 'Hide History' : 'Show History' }}
    </button>

    <!-- Added Chat History Component -->
    <ChatHistory 
      v-if="showHistory" 
      :history="chatHistory" 
    />
  </div>
</template>

<script>
import VoiceInput from './VoiceInput.vue';
import TextOutput from './TextOutput.vue';
import ErrorMessage from './ErrorMessage.vue'; // Added ErrorMessage component
import ChatHistory from './ChatHistory.vue'; // Added ChatHistory component

export default {
  components: {
    VoiceInput,
    TextOutput,
    ErrorMessage,
    ChatHistory,
  },
  data() {
    return {
      textOutput: '', // Stores the processed text output
      isLoading: false, // Tracks whether the request is being processed
      errorMessage: '', // Added for error handling
      showHistory: false, // Added to toggle chat history
      chatHistory: [], // Added to store chat history
    };
  },
  methods: {
    async handleVoiceInput(audio) {
      try {
        this.isLoading = true; // Show loading state
        this.errorMessage = ''; // Clear any previous errors
        const response = await fetch('/voice-to-text', {
          method: 'POST',
          headers: {
            'Content-Type': 'audio/wav', // Ensure appropriate content type
          },
          body: audio, // Send audio blob
        });

        if (!response.ok) {
          throw new Error('Failed to process audio.');
        }

        const data = await response.json();
        this.textOutput = data.text; // Update text output with the response
        this.chatHistory.push({ type: 'user', text: 'Voice input' }); // Add user input to history
        this.chatHistory.push({ type: 'system', text: data.text }); // Add system response to history
      } catch (error) {
        console.error('Error processing audio:', error);
        this.errorMessage = 'Error: Unable to process your input.'; // Set error message
      } finally {
        this.isLoading = false; // Reset loading state
      }
    },
    clearError() {
      this.errorMessage = ''; // Clear error message
    },
    toggleHistory() {
      this.showHistory = !this.showHistory; // Toggle chat history visibility
    },
  },
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.loading-spinner {
  margin-top: 20px;
  font-size: 1.2rem;
  color: #555;
}

.history-toggle {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.history-toggle:hover {
  background-color: #0056b3;
}
</style>
