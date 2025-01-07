<template>
  <div class="voice-input-container">
    <button 
      :disabled="isRecording" 
      @click="startRecording" 
      class="record-button"
    >
      {{ isRecording ? "Recording..." : "Start Recording" }}
    </button>
    <button 
      v-if="isRecording" 
      @click="stopRecording" 
      class="stop-button"
    >
      Stop Recording
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isRecording: false,
      mediaRecorder: null,
      audioChunks: [],
    };
  },
  methods: {
    async startRecording() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        this.mediaRecorder = new MediaRecorder(stream);
        this.audioChunks = [];
        this.isRecording = true;

        this.mediaRecorder.ondataavailable = (event) => {
          if (event.data.size > 0) {
            this.audioChunks.push(event.data);
          }
        };

        this.mediaRecorder.onstop = () => {
          const audioBlob = new Blob(this.audioChunks, { type: "audio/wav" });
          this.$emit("voiceInput", audioBlob);
          this.audioChunks = [];
        };

        this.mediaRecorder.start();
      } catch (error) {
        console.error("Error accessing microphone:", error);
        alert("Unable to access microphone. Please check your permissions.");
      }
    },
    stopRecording() {
      if (this.mediaRecorder) {
        this.mediaRecorder.stop();
        this.isRecording = false;
      }
    },
  },
};
</script>

<style scoped>
.voice-input-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.record-button,
.stop-button {
  padding: 10px 20px;
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.record-button {
  background-color: #4caf50;
  color: white;
}

.record-button:disabled {
  background-color: #9e9e9e;
  cursor: not-allowed;
}

.stop-button {
  background-color: #f44336;
  color: white;
}

.stop-button:hover {
  background-color: #d32f2f;
}
</style>
