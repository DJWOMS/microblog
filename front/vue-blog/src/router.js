import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import MyTweets from './components/MyTweets'
import store from './store'
Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/my/:id',
            name: 'my_tweets',
            component: MyTweets,
            beforeEnter: (to, from, next) => {
                if (store.getters.get_auth) {
                    next()
                } else {
                    next({name: 'home'})
                }
            }
        },
    ]
})

