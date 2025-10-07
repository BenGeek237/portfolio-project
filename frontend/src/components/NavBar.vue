<template>
  <nav class="fixed top-0 left-0 w-full z-50 transition-all duration-500"
       :class="scrolled ? 'py-3 bg-white/95 backdrop-blur-lg shadow-lg' : 'py-4 sm:py-6 bg-transparent'">
    <div class="container mx-auto px-4 sm:px-6">
      <div class="flex justify-between items-center">
        <!-- Logo -->
        <a href="#" class="flex items-center space-x-2 group">
          <div class="w-8 sm:w-10 h-8 sm:h-10 rounded-xl bg-gradient-to-r from-primary to-secondary flex items-center justify-center shadow-lg">
            <span class="text-white font-bold text-base sm:text-lg">M</span>
          </div>
          <span class="text-xl sm:text-2xl font-bold text-dark group-hover:text-primary transition-colors duration-300">Mamoudou</span>
        </a>

        <!-- Menu Desktop -->
        <div class="hidden lg:flex items-center space-x-1">
          <a v-for="(item, index) in navItems" 
             :key="index"
             :href="item.link" 
             class="relative px-3 sm:px-5 py-2 sm:py-3 font-medium text-gray-700 rounded-xl transition-all duration-300 group"
             :class="activeSection === item.id ? 
                    'text-primary bg-primary/10 shadow-md' : 
                    'hover:text-primary hover:bg-light'"
             @click="setActiveSection(item.id)">
            <span class="relative z-10">{{ item.name }}</span>
            <div v-if="activeSection === item.id" 
                 class="absolute inset-0 bg-gradient-to-r from-primary/10 to-secondary/10 rounded-xl animate-pulse"></div>
            <div v-if="activeSection === item.id" 
                 class="absolute bottom-0 left-1/2 transform -translate-x-1/2 w-1 h-1 bg-primary rounded-full"></div>
          </a>
          <a href="#contact" 
             class="ml-4 px-4 sm:px-6 py-2 sm:py-3 bg-gradient-to-r from-primary to-secondary text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 hover-lift">
            Contact
          </a>
        </div>

        <!-- Menu Mobile Button -->
        <button @click="toggleMobileMenu" 
                class="lg:hidden w-10 sm:w-12 h-10 sm:h-12 rounded-xl bg-light flex items-center justify-center text-gray-700 hover:bg-primary hover:text-white transition-all duration-300 shadow-sm">
          <i class="fas fa-bars text-lg sm:text-xl"></i>
        </button>
      </div>

      <!-- Menu Mobile -->
      <div v-if="mobileMenuOpen" 
           class="lg:hidden mt-4 bg-white rounded-2xl shadow-2xl p-4 sm:p-6 animate-slide-down border border-gray-100">
        <div class="flex flex-col space-y-3">
          <a v-for="(item, index) in navItems" 
             :key="index"
             :href="item.link" 
             class="px-4 py-3 rounded-xl font-medium transition-all duration-300 flex items-center"
             :class="activeSection === item.id ? 
                    'text-primary bg-primary/10' : 
                    'text-gray-700 hover:text-primary hover:bg-light'"
             @click="setActiveSection(item.id); mobileMenuOpen = false">
            <i :class="item.icon" class="w-6 mr-3 text-center"></i>
            <span>{{ item.name }}</span>
            <div v-if="activeSection === item.id" 
                 class="ml-auto w-2 h-2 bg-primary rounded-full"></div>
          </a>
          <div class="border-t border-gray-200 my-2"></div>
          <a href="#contact" 
             class="px-4 py-3 bg-gradient-to-r from-primary to-secondary text-white font-semibold rounded-xl text-center shadow-lg mt-2"
             @click="mobileMenuOpen = false">
            Me Contacter
          </a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      scrolled: false,
      mobileMenuOpen: false,
      activeSection: 'accueil',
      navItems: [
        { id: 'accueil', name: 'Accueil', link: '#accueil', icon: 'fas fa-home' },
        { id: 'apropos', name: 'À propos', link: '#apropos', icon: 'fas fa-user' },
        { id: 'projets', name: 'Projets', link: '#projets', icon: 'fas fa-briefcase' },
        { id: 'contact', name: 'Contact', link: '#contact', icon: 'fas fa-envelope' },
      ],
    }
  },
  methods: {
    handleScroll() {
      this.scrolled = window.scrollY > 50;
      const sections = ['accueil', 'apropos', 'projets', 'contact'];
      const scrollPosition = window.scrollY + 100;

      for (const section of sections) {
        const element = document.getElementById(section);
        if (element) {
          const offsetTop = element.offsetTop;
          const offsetBottom = offsetTop + element.offsetHeight;

          if (scrollPosition >= offsetTop && scrollPosition < offsetBottom) {
            this.activeSection = section;
            break;
          }
        }
      }
    },
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen;
    },
    setActiveSection(section) {
      this.activeSection = section;
    },
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
    this.handleScroll();
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
}
</script>