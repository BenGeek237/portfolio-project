<template>
  <section id="apropos" class="py-20 bg-white">
    <div class="container mx-auto px-6">
      <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 text-dark">
        À <span class="text-gradient">Propos</span>
      </h2>
      <div v-if="loading" class="text-center text-gray-600">Chargement...</div>
      <div v-else-if="error" class="text-center text-red-600">{{ error }}</div>
      <div v-else class="flex flex-col md:flex-row items-center gap-12">
        <div class="md:w-1/2">
          <img src="https://via.placeholder.com/400" 
               alt="Mamoudou" 
               class="rounded-2xl shadow-xl w-full max-w-md mx-auto">
        </div>
        <div class="md:w-1/2">
          <h3 class="text-2xl font-semibold text-dark mb-4">Mamoudou, Développeur Web</h3>
          <p class="text-gray-600 mb-6 leading-relaxed">
            Je suis un développeur web passionné par la création d'interfaces modernes et intuitives. 
            Avec une expertise en Vue.js, Django, et Tailwind CSS, je transforme des idées en expériences digitales uniques.
          </p>
          <div class="grid grid-cols-2 gap-4">
            <div v-for="(skill, index) in skills" 
                 :key="index"
                 class="flex items-center space-x-3 bg-light p-4 rounded-xl shadow-sm hover-lift">
              <i :class="skill.icon" class="text-primary text-2xl"></i>
              <span class="text-gray-700 font-medium">{{ skill.name }}</span>
            </div>
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
      skills: [],
      loading: false,
      error: null,
    }
  },
  async created() {
    this.loading = true
    try {
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/skills/`)
      this.skills = response.data
    } catch (err) {
      this.error = `Erreur lors du chargement des compétences : ${err.message}`
      console.error('Erreur API :', err)
    } finally {
      this.loading = false
    }
  },
}
</script>