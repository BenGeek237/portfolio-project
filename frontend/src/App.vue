<template>
  <div class="font-sans bg-light text-gray-800 overflow-x-hidden">
    <NavBar />
    <main>
      <section id="accueil" class="min-h-screen flex items-center pt-20 relative overflow-hidden bg-gradient-to-br from-primary/10 via-secondary/10 to-light">
        <div class="bubbles-container">
          <div v-for="n in 10" :key="n" class="bubble" :style="bubbleStyles(n)"></div>
        </div>
        <div class="container mx-auto px-6 relative z-10">
          <div class="max-w-lg md:max-w-xl">
            <h1 class="text-4xl sm:text-5xl md:text-7xl font-bold mb-6 leading-tight animate-slide-in">
              <span class="text-gradient">Créateur</span><br>
              d'expériences<br>
              digitales mémorables
            </h1>
            <p class="text-lg sm:text-xl text-gray-600 mb-8 leading-relaxed animate-fade-in">
              Bienvenue sur mon portfolio ! Je suis Mamoudou, passionné par le design et le développement web.
            </p>
            <a href="#contact" 
               class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-primary to-secondary text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 hover-lift">
              Me Contacter
              <i class="fas fa-arrow-right ml-2"></i>
            </a>
          </div>
        </div>
      </section>
      <About />
      <Projects />
      <Contact />
    </main>
    <Footer />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import About from './components/About.vue'
import Projects from './components/Projects.vue'
import Contact from './components/Contact.vue'
import Footer from './components/Footer.vue'

export default {
  components: {
    NavBar,
    About,
    Projects,
    Contact,
    Footer,
  },
  methods: {
    bubbleStyles(index) {
      const sizes = [30, 50, 80, 40, 60, 25, 70, 45, 90, 35]
      const delays = [0, 1, 2, 0.5, 1.5, 3, 2.5, 1.2, 2.8, 0.8]
      const positions = [
        { top: '10%', left: '15%' },
        { top: '20%', left: '70%' },
        { top: '35%', left: '30%' },
        { top: '60%', left: '85%' },
        { top: '25%', left: '50%' },
        { top: '70%', left: '20%' },
        { top: '45%', left: '75%' },
        { top: '80%', left: '40%' },
        { top: '15%', left: '90%' },
        { top: '50%', left: '10%' },
      ]
      return {
        width: `${sizes[index - 1]}px`,
        height: `${sizes[index - 1]}px`,
        top: positions[index - 1].top,
        left: positions[index - 1].left,
        animationDelay: `${delays[index - 1]}s`,
      }
    },
  },
}
</script>

<style scoped>
.bubbles-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  overflow: hidden;
}

.bubble {
  position: absolute;
  background: linear-gradient(45deg, rgba(108, 99, 255, 0.5), rgba(74, 68, 198, 0.5));
  border-radius: 50%;
  opacity: 0.5;
  animation: float 8s ease-in-out infinite;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-30px); }
}

@media (max-width: 768px) {
  .bubbles-container {
    transform: scale(0.8);
  }
  .bubble {
    transform: scale(0.7);
  }
  .max-w-lg {
    max-width: 100%;
  }
}
</style>