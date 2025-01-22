<template>
  <div class="about-container">
    <!-- About Section -->
    <section class="about-section">
      <h1>About ZephyrNet HumanoidChat</h1>
      <p>
        ZephyrNet HumanoidChat is a cutting-edge AI-powered communication tool designed to provide seamless and intelligent interactions. 
        Whether you're looking for voice-to-text transcription, text-to-speech synthesis, or real-time translation, our platform has you covered.
      </p>
      <p>
        Our mission is to make communication more accessible, efficient, and enjoyable for everyone. With advanced natural language processing 
        and state-of-the-art AI models, we aim to bridge the gap between humans and technology.
      </p>
    </section>

    <!-- Team Section -->
    <section class="team-section">
      <h2>Meet the Team</h2>
      <div class="team-grid">
        <div class="team-member">
          <img src="@/assets/team-member1.jpg" alt="Team Member 1" />
          <h3>John Doe</h3>
          <p>Lead Developer</p>
        </div>
        <div class="team-member">
          <img src="@/assets/team-member2.jpg" alt="Team Member 2" />
          <h3>Jane Smith</h3>
          <p>AI Engineer</p>
        </div>
        <div class="team-member">
          <img src="@/assets/team-member3.jpg" alt="Team Member 3" />
          <h3>Alice Johnson</h3>
          <p>UX Designer</p>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section">
      <h2>Contact Us</h2>
      <p>
        Have questions or feedback? We'd love to hear from you! Reach out to us at 
        <a href="mailto:support@zephyrnet.com">support@zephyrnet.com</a>.
      </p>
    </section>

    <!-- Added FAQ Section -->
    <section class="faq-section">
      <h2>Frequently Asked Questions</h2>
      <div class="faq-list">
        <div class="faq-item">
          <h3>How does ZephyrNet HumanoidChat work?</h3>
          <p>
            ZephyrNet HumanoidChat uses advanced AI models to process voice, text, and translation requests in real-time. 
            Our system is designed to be fast, accurate, and user-friendly.
          </p>
        </div>
        <div class="faq-item">
          <h3>Is my data secure?</h3>
          <p>
            Yes, we take data security very seriously. All communications are encrypted, and we adhere to strict privacy policies 
            to ensure your information is safe.
          </p>
        </div>
        <div class="faq-item">
          <h3>Can I use ZephyrNet HumanoidChat for free?</h3>
          <p>
            Yes, we offer a free tier with basic features. For advanced functionality, you can upgrade to our premium plan.
          </p>
        </div>
      </div>
    </section>

    <!-- Added Newsletter Subscription -->
    <section class="newsletter-section">
      <h2>Subscribe to Our Newsletter</h2>
      <p>Stay updated with the latest features, news, and updates from ZephyrNet HumanoidChat.</p>
      <form @submit.prevent="subscribeNewsletter">
        <input 
          type="email" 
          v-model="email" 
          placeholder="Enter your email" 
          required 
        />
        <button type="submit">Subscribe</button>
      </form>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '', // Added for newsletter subscription
    };
  },
  methods: {
    subscribeNewsletter() {
      // Simulate newsletter subscription
      alert(`Thank you for subscribing, ${this.email}!`);
      this.email = ''; // Reset email input
    },
  },
};
</script>

<style scoped>
.about-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.about-section,
.team-section,
.contact-section,
.faq-section,
.newsletter-section {
  margin-bottom: 40px;
}

h1, h2 {
  color: #333;
  margin-bottom: 20px;
}

p {
  color: #555;
  line-height: 1.6;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.team-member {
  text-align: center;
}

.team-member img {
  width: 100%;
  max-width: 150px;
  border-radius: 50%;
  margin-bottom: 10px;
}

.team-member h3 {
  margin: 10px 0 5px;
  color: #333;
}

.team-member p {
  color: #777;
}

.faq-list {
  margin-top: 20px;
}

.faq-item {
  margin-bottom: 20px;
}

.faq-item h3 {
  color: #333;
  margin-bottom: 10px;
}

.newsletter-section form {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.newsletter-section input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.newsletter-section button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.newsletter-section button:hover {
  background-color: #0056b3;
}
</style>
