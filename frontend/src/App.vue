<template>
  <div class="font-sans bg-light text-gray-800 overflow-x-hidden">
    <NavBar />
    <main>
      <section id="accueil" class="min-h-screen flex items-center pt-20 relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-animated opacity-10 z-0"></div>
        <div class="absolute inset-0 overflow-hidden z-0">
          <div v-for="i in 15" :key="i" 
               class="absolute rounded-full bg-primary/10"
               :class="floatingElements[i-1]"
               :style="`animation-delay: ${i * 0.5}s`"></div>
        </div>
        <div class="container mx-auto px-6 relative z-10">
          <div class="max-w-2xl">
            <h1 class="text-5xl md:text-7xl font-bold mb-6 leading-tight">
              <span class="text-gradient">Créateur</span><br>
              d'expériences<br>
              digitales mémorables
            </h1>
            <p class="text-xl text-gray-600 mb-8 leading-relaxed">
              Je suis designer et développeur passionné par la création d'interfaces modernes et intuitives qui allient esthétique et fonctionnalité.
            </p>
            <div class="flex flex-wrap gap-4">
              <a href="#projets" 
                 class="px-8 py-4 bg-primary text-white font-semibold rounded-xl shadow-lg hover-lift hover:shadow-xl transition-all duration-300 animate-glow">
                Voir mes projets
              </a>
              <a href="#contact" 
                 class="px-8 py-4 border-2 border-primary text-primary font-semibold rounded-xl hover-lift transition-all duration-300">
                Me contacter
              </a>
            </div>
          </div>
        </div>
        <div class="hidden lg:block absolute right-0 top-1/2 -translate-y-1/2 w-2/5 h-4/5 z-0">
          <div class="w-full h-full bg-gradient-to-br from-primary to-secondary rounded-l-3xl relative overflow-hidden">
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
              <div class="cube">
                <div class="face front"></div>
                <div class="face back"></div>
                <div class="face right"></div>
                <div class="face left"></div>
                <div class="face top"></div>
                <div class="face bottom"></div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- Autres sections (À propos, Projets, Contact, Footer) à ajouter si besoin -->
    </main>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  components: {
    NavBar,
  },
  data() {
    return {
      floatingElements: [
        'w-20 h-20 top-1/4 left-1/4 animate-float',
        'w-32 h-32 top-3/4 left-3/4 animate-float',
        'w-16 h-16 top-1/2 left-4/5 animate-float',
        'w-24 h-24 top-1/3 left-1/5 animate-float',
        'w-28 h-28 top-2/3 left-2/5 animate-float',
        'w-12 h-12 top-1/5 left-3/5 animate-float',
        'w-36 h-36 top-4/5 left-1/10 animate-float',
        'w-14 h-14 top-3/5 left-7/10 animate-float',
        'w-22 h-22 top-2/5 left-9/10 animate-float',
        'w-18 h-18 top-4/5 left-4/5 animate-float',
        'w-26 h-26 top-1/10 left-1/2 animate-float',
        'w-10 h-10 top-3/4 left-1/10 animate-float',
        'w-30 h-30 top-1/2 left-1/10 animate-float',
        'w-8 h-8 top-1/4 left-3/4 animate-float',
        'w-34 h-34 top-2/3 left-9/10 animate-float',
      ],
    }
  },
}
</script>

<style scoped>
.cube {
  width: 100px;
  height: 100px;
  position: relative;
  transform-style: preserve-3d;
  animation: rotate 10s infinite linear;
}

.face {
  position: absolute;
  width: 100px;
  height: 100px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.front { transform: translateZ(50px); }
.back { transform: translateZ(-50px) rotateY(180deg); }
.right { transform: rotateY(90deg) translateZ(50px); }
.left { transform: rotateY(-90deg) translateZ(50px); }
.top { transform: rotateX(90deg) translateZ(50px); }
.bottom { transform: rotateX(-90deg) translateZ(50px); }

@keyframes rotate {
  from { transform: rotateX(0) rotateY(0) rotateZ(0); }
  to { transform: rotateX(360deg) rotateY(360deg) rotateZ(360deg); }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(10deg); }
}

.bg-gradient-animated {
  background: linear-gradient(-45deg, #6C63FF, #4A44C6, #FF6584, #6C63FF);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
}

@keyframes gradient {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
</style>