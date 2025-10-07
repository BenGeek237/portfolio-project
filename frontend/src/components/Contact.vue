<template>
  <section id="contact" class="py-20 bg-dark text-white">
    <div class="container mx-auto px-6">
      <h2 class="text-4xl md:text-5xl font-bold text-center mb-16">
        Me <span class="text-gradient">Contacter</span>
      </h2>
      <div v-if="loading" class="text-center text-gray-400">Chargement...</div>
      <div v-else-if="error" class="text-center text-red-600">{{ error }}</div>
      <div v-else class="max-w-2xl mx-auto">
        <form @submit.prevent="submitForm" class="space-y-6">
          <div>
            <label for="name" class="block text-sm font-medium mb-2">Nom</label>
            <input type="text" id="name" v-model.trim="form.name" 
                   class="w-full px-4 py-3 rounded-xl bg-light/10 border"
                   :class="errors.name ? 'border-red-500 focus:ring-red-500' : 'border-white/20 focus:ring-primary'"
                   @input="validateField('name')">
            <p v-if="errors.name" class="text-red-500 text-sm mt-1">{{ errors.name }}</p>
          </div>
          <div>
            <label for="email" class="block text-sm font-medium mb-2">Email</label>
            <input type="email" id="email" v-model.trim="form.email" 
                   class="w-full px-4 py-3 rounded-xl bg-light/10 border"
                   :class="errors.email ? 'border-red-500 focus:ring-red-500' : 'border-white/20 focus:ring-primary'"
                   @input="validateField('email')">
            <p v-if="errors.email" class="text-red-500 text-sm mt-1">{{ errors.email }}</p>
          </div>
          <div>
            <label for="message" class="block text-sm font-medium mb-2">Message</label>
            <textarea id="message" v-model.trim="form.message" rows="5"
                      class="w-full px-4 py-3 rounded-xl bg-light/10 border"
                      :class="errors.message ? 'border-red-500 focus:ring-red-500' : 'border-white/20 focus:ring-primary'"
                      @input="validateField('message')"></textarea>
            <p v-if="errors.message" class="text-red-500 text-sm mt-1">{{ errors.message }}</p>
          </div>
          <button type="submit" 
                  :disabled="formSubmitting || !isFormValid"
                  class="w-full px-6 py-3 bg-gradient-to-r text-white font-semibold rounded-xl shadow-lg transition-all duration-300 hover-lift"
                  :class="formSubmitting || !isFormValid ? 'from-gray-400 to-gray-500 cursor-not-allowed' : 'from-primary to-secondary hover:shadow-xl'">
            {{ formSubmitting ? 'Envoi en cours...' : 'Envoyer' }}
          </button>
          <p v-if="formSuccess" class="text-center text-green-400 mt-4">Message envoyé avec succès !</p>
          <p v-if="formError" class="text-center text-red-600 mt-4">{{ formError }}</p>
        </form>
        <div class="mt-8 flex flex-wrap justify-center gap-6">
          <a v-for="(contact, index) in contacts" 
             :key="index"
             :href="contact.value"
             target="_blank"
             class="flex items-center space-x-3 text-white hover:text-primary transition-colors duration-300">
            <i :class="contact.icon" class="text-xl"></i>
            <span>{{ contact.type }}</span>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      form: {
        name: '',
        email: '',
        message: '',
      },
      errors: {
        name: null,
        email: null,
        message: null,
      },
      contacts: [],
      loading: false,
      error: null,
      formSubmitting: false,
      formSuccess: false,
      formError: null,
    }
  },
  computed: {
    isFormValid() {
      return !this.errors.name && !this.errors.email && !this.errors.message && 
             this.form.name && this.form.email && this.form.message
    },
  },
  async created() {
    this.loading = true
    try {
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/contact-details/`)
      this.contacts = response.data
    } catch (err) {
      this.error = `Erreur lors du chargement des contacts : ${err.message}`
      console.error('Erreur API :', err)
    } finally {
      this.loading = false
    }
  },
  methods: {
    validateField(field) {
      if (field === 'name') {
        this.errors.name = this.form.name ? null : 'Le nom est requis.'
      }
      if (field === 'email') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        this.errors.email = this.form.email 
          ? (emailRegex.test(this.form.email) ? null : 'Veuillez entrer un email valide.')
          : 'L\'email est requis.'
      }
      if (field === 'message') {
        this.errors.message = this.form.message ? null : 'Le message est requis.'
      }
    },
    validateForm() {
      this.validateField('name')
      this.validateField('email')
      this.validateField('message')
      return this.isFormValid
    },
    async submitForm() {
      if (!this.validateForm()) return
      this.formSubmitting = true
      this.formSuccess = false
      this.formError = null
      try {
        await axios.post(`${import.meta.env.VITE_API_URL}/api/messages/`, this.form)
        this.formSuccess = true
        this.form = { name: '', email: '', message: '' }
        this.errors = { name: null, email: null, message: null }
      } catch (err) {
        this.formError = `Erreur lors de l'envoi du message : ${err.message}`
        console.error('Erreur API :', err)
      } finally {
        this.formSubmitting = false
      }
    },
  },
}
</script>