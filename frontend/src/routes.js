import Game from './components/Game.vue'
import Home from './components/Home.vue'
import NotFound from './components/NotFound.vue'

export const routes = [
    { path: '', component:  Home },
    { path: '/urlgame', component:  Game },
    { path: '*', component: NotFound }
]