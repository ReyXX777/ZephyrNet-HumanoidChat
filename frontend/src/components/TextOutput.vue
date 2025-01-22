<template>
  <div class="text-output-container">
    <div v-if="text && !isError" class="text-output">
      <p>{{ text }}</p>
      <!-- Added Copy to Clipboard Button -->
      <button 
        class="copy-button" 
        @click="copyToClipboard" 
        aria-label="Copy text to clipboard"
      >
        Copy Text
      </button>
    </div>
    <div v-else-if="isError" class="error-message">
      <p>{{ errorMessage }}</p>
      <!-- Added Retry Button for Errors -->
      <button 
        class="retry-button" 
        @click="handleRetry" 
        aria-label="Retry processing"
      >
        Retry
      </button>
    </div>
    <div v-else class="placeholder">
      <p>Processed text will appear here...</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      default: '',
      description: 'The processed text to display.',
    },
    isError: {
      type: Boolean,
      default: false,
      description: 'Indicates if an error occurred during processing.',
    },
    errorMessage: {
      type: String,
      default: 'An error occurred while processing the text.',
      description: 'Custom error message to display when an error occurs.',
    },
  },
  methods: {
    copyToClipboard() {
      navigator.clipboard.writeText(this.text)
        .then(() => {
          alert('Text copied to clipboard!');
        })
        .catch(() => {
          alert('Failed to copy text.');
        });
    },
    handleRetry() {
      this.$emit('retry'); // Emit retry event to parent component
    },
  },
};
</script>

<style scoped>
.text-output-container {
  width: 100%;
  max-width: 600px;
  margin: 20px auto;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  font-family: Arial, sans-serif;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.text-output {
  font-size: 1rem;
  color: #333;
  line-height: 1.5;
}

.error-message {
  font-size: 1rem;
  color: #d9534f;
  font-weight: bold;
  text-align: center;
}

.placeholder {
  font-size: 0.9rem;
  color: #999;
  text-align: center;
}

.copy-button {
  margin-top: 10px;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.copy-button:hover {
  background-color: #0056b3;
}

.retry-button {
  margin-top: 10px;
  padding: 8px 16px;
  background-color: #d9534f;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.retry-button:hover {
  background-color: #c9302c;
}
</style>
