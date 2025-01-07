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
  </div>
</template>

<script>
import VoiceInput from './VoiceInput.vue';
import TextOutput from './TextOutput.vue';

export default {
  components: {
    VoiceInput,
    TextOutput,
  },
  data() {
    return {
      textOutput: '', // Stores the processed text output
      isLoading: false, // Tracks whether the request is being processed
    };
  },
  methods: {
    async handleVoiceInput(audio) {
      try {
        this.isLoading = true; // Show loading state
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
      } catch (error) {
        console.error('Error processing audio:', error);
        this.textOutput = 'Error: Unable to process your input.';
      } finally {
        this.isLoading = false; // Reset loading state
      }
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
</style>
