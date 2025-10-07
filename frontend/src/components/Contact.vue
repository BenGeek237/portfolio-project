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
            <input type="text" id="name" v-model="form.name" 
                   class="w-full px-4 py-3 rounded-xl bg-light/10 border border-white/20 focus:outline-none focus:ring-2 focus:ring-primary">
          </div>
          <div>
            <label for="email" class="block text-sm font-medium mb-2">Email</label>
            <input type="email" id="email" v-model="form.email" 
                   class="w-full px-4 py-3 rounded-xl bg-light/10 border border-white/20 focus:outline-none focus:ring-2 focus:ring-primary">
          </div>
          <div>
            <label for="message" class="block text-sm font-medium mb-2">Message</label>
            <textarea id="message" v-model="form.message" rows="5"
                      class="w-full px-4 py-3 rounded-xl bg-light/10 border border-white/20 focus:outline-none focus:ring-2 focus:ring-primary"></textarea>
          </div>
          <button type="submit" 
                  :disabled="formSubmitting"
                  class="w-full px-6 py-3 bg-gradient-to-r from-primary to-secondary text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 hover-lift">
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
      contacts: [],
      loading: false,
      error: null,
      formSubmitting: false,
      formSuccess: false,
      formError: null,
    }
  },
  async created() {
    this.loading = true
    try {
      const response = await axios.get('http://localhost:8000/api/contact-details/')
      this.contacts = response.data
    } catch (err) {
      this.error = `Erreur lors du chargement des contacts : ${err.message}`
      console.error('Erreur API :', err)
    } finally {
      this.loading = false
    }
  },
  methods: {
    async submitForm() {
      this.formSubmitting = true
      this.formSuccess = false
      this.formError = null
      try {
        await axios.post('http://localhost:8000/api/messages/', this.form)
        this.formSuccess = true
        this.form = { name: '', email: '', message: '' }
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