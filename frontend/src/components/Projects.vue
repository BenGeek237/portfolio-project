<template>
  <section id="projets" class="py-20 bg-light">
    <div class="container mx-auto px-6">
      <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 text-dark">
        Mes <span class="text-gradient">Projets</span>
      </h2>
      <div v-if="loading" class="text-center text-gray-600">Chargement...</div>
      <div v-else-if="error" class="text-center text-red-600">{{ error }}</div>
      <div v-else-if="projects.length === 0" class="text-center text-gray-600">Aucun projet disponible.</div>
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="(project, index) in projects" 
             :key="index"
             class="group bg-white rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-500 hover-lift overflow-hidden">
          <div class="relative h-48 overflow-hidden">
            <img :src="project.image" 
                 :alt="project.title" 
                 class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-dark/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </div>
          <div class="p-6">
            <h3 class="text-xl font-semibold text-dark mb-3">{{ project.title }}</h3>
            <p class="text-gray-600 mb-4">{{ project.description }}</p>
            <div class="flex flex-wrap gap-2 mb-4">
              <span v-for="(tag, tagIndex) in project.tags" 
                    :key="tagIndex"
                    class="px-3 py-1 bg-primary/10 text-primary text-sm rounded-full">
                {{ tag }}
              </span>
            </div>
            <a :href="project.link" 
               target="_blank" 
               class="inline-flex items-center px-4 py-2 bg-primary text-white font-semibold rounded-xl hover:bg-secondary transition-colors duration-300">
              Voir le projet
              <i class="fas fa-arrow-right ml-2"></i>
            </a>
          </div>
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
      projects: [],
      loading: false,
      error: null,
    }
  },
  async created() {
    this.loading = true
    try {
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/projects/`)
      this.projects = response.data
    } catch (err) {
      this.error = `Erreur lors du chargement des projets : ${err.message}. Vérifiez que le serveur Django est en cours d'exécution.`
      console.error('Erreur API :', err)
    } finally {
      this.loading = false
    }
  },
}
</script>