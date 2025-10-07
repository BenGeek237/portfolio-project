<template>
  <div class="font-sans bg-light text-gray-800 overflow-x-hidden">
    <NavBar />
    <main>
      <section id="accueil" class="min-h-screen flex items-center pt-20 relative">
        <div class="container mx-auto px-6 flex flex-col md:flex-row items-center gap-12">
          <div class="md:w-1/2">
            <h1 class="text-5xl md:text-7xl font-bold mb-6 leading-tight animate-slide-in">
              <span class="text-gradient">Créateur</span><br>
              d'expériences<br>
              digitales mémorables
            </h1>
            <p class="text-xl text-gray-600 mb-8 leading-relaxed animate-fade-in">
              Bienvenue sur mon portfolio ! Je suis Mamoudou, passionné par le design et le développement web.
            </p>
            <a href="#contact" 
               class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-primary to-secondary text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 hover-lift">
              Me Contacter
              <i class="fas fa-arrow-right ml-2"></i>
            </a>
          </div>
          <div class="md:w-1/2 relative">
            <div class="cube-container">
              <div class="cube">
                <div class="cube-face front"></div>
                <div class="cube-face back"></div>
                <div class="cube-face right"></div>
                <div class="cube-face left"></div>
                <div class="cube-face top"></div>
                <div class="cube-face bottom"></div>
              </div>
            </div>
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
}
</script>

<style scoped>
.cube-container {
  perspective: 1000px;
  width: 300px;
  height: 300px;
  margin: 0 auto;
}

.cube {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  animation: rotate 20s infinite linear;
}

.cube-face {
  position: absolute;
  width: 300px;
  height: 300px;
  background: linear-gradient(45deg, rgba(108, 99, 255, 0.7), rgba(74, 68, 198, 0.7));
  border: 2px solid rgba(255, 255, 255, 0.2);
  opacity: 0.8;
}

.front  { transform: translateZ(150px); }
.back   { transform: translateZ(-150px) rotateY(180deg); }
.right  { transform: translateX(150px) rotateY(90deg); }
.left   { transform: translateX(-150px) rotateY(-90deg); }
.top    { transform: translateY(-150px) rotateX(90deg); }
.bottom { transform: translateY(150px) rotateX(-90deg); }

@keyframes rotate {
  0% { transform: rotateX(0deg) rotateY(0deg); }
  100% { transform: rotateX(360deg) rotateY(360deg); }
}
</style>