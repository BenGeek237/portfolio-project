<template>
  <footer class="py-8 bg-dark text-white">
    <div class="container mx-auto px-6 text-center">
      <div v-if="loading" class="text-gray-400">Chargement...</div>
      <div v-else-if="error" class="text-red-600">{{ error }}</div>
      <div v-else>
        <p class="text-gray-400 mb-4">© 2025 Mamoudou. Tous droits réservés.</p>
        <div class="flex justify-center gap-6">
          <a v-for="(link, index) in socialLinks" 
             :key="index"
             :href="link.link"
             target="_blank"
             class="text-white hover:text-primary transition-colors duration-300">
            <i :class="link.icon" class="text-xl"></i>
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      socialLinks: [],
      loading: false,
      error: null,
    }
  },
  async created() {
    this.loading = true
    try {
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/social-links/`)
      this.socialLinks = response.data
    } catch (err) {
      this.error = `Erreur lors du chargement des liens sociaux : ${err.message}`
      console.error('Erreur API :', err)
    } finally {
      this.loading = false
    }
  },
}
</script>