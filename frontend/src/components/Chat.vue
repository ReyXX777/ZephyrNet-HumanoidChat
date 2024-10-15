<template>
    <div class="chat-container">
      <VoiceInput @voiceInput="handleVoiceInput" />
      <TextOutput :text="textOutput" />
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
        textOutput: '',
      };
    },
    methods: {
      async handleVoiceInput(audio) {
        const response = await fetch('/voice-to-text', {
          method: 'POST',
          body: audio,
        });
        const data = await response.json();
        this.textOutput = data.text;
      },
    },
  };
  </script>
  
  <style>
  .chat-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }
  </style>
  