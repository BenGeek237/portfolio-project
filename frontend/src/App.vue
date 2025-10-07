<template>
  <div class="font-sans bg-light text-gray-800 overflow-x-hidden">
    <NavBar />
    <!-- Placeholder pour les autres sections -->
    <main>
      <section id="accueil" class="min-h-screen flex items-center pt-20">
        <div class="container mx-auto px-6">
          <h1 class="text-5xl md:text-7xl font-bold mb-6 leading-tight">
            <span class="text-gradient">Créateur</span><br>
            d'expériences<br>
            digitales mémorables
          </h1>
          <p class="text-xl text-gray-600 mb-8 leading-relaxed">
            Bienvenue sur mon portfolio ! (Sections à venir...)
          </p>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  components: {
    NavBar,
  },
}
</script>