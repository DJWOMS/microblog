<template>
    <div class="navbar navbar-expand-lg navbar-dark menu">
        <!-- Collapse button -->
        <button class="navbar-toggler" type="button" data-toggle="collapse"
                data-target="#basicExampleNav"
                aria-controls="basicExampleNav" aria-expanded="false"
                aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="basicExampleNav">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#" @click="goPage('home')">Главная</a>
                </li>
            </ul>
            <ul class="navbar-nav mr-0">
                <!--{% if user.is_authenticated %}-->
                <li class="nav-item">
                    <a v-if="auth" class="nav-link" href="#">My Posts + Whom I follow
                    </a>
                </li>
                <li class="nav-item my-0">
                    <a v-if="auth"  @click="goPage('my_tweets')" class="nav-link" href="#">Мои записи</a>
                </li>
                <li class="nav-item my-0">
                    <a class="nav-link"
                       href="#">
                        <!--<span>{{ user.username }}</span>-->
                    </a>
                </li>
                <li class="nav-item my-0">
                    <img class="avatar" src="">
                </li>
                <li class="nav-item my-0">
                    <a v-if="auth" @click="logout" class="nav-link" href="#">Выход</a>
                </li>
                <!--{% else %}-->
                <li class="nav-item my-0">
                    <a v-if="!auth"
                       @click="goLogin"
                       class="nav-link"
                       href="#"
                       data-toggle="modal"
                       data-target="#loginModal">
                        Вход
                    </a>
                </li>
                <!--{% endif %}-->
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Menu",
        computed: {
            auth() {
                if (this.$store.getters.get_auth) return true
                else return false
            }
        },
        methods: {
            goPage(item) {
                this.$router.push({name: item})
            },
            goLogin() {
                this.$emit("showLogin")
            },
            logout() {
                this.$store.commit("set_auth", false)
                sessionStorage.removeItem("token")
                $.ajaxSetup({
                    headers: {'Authorization': ""},
                });
                window.location = '/'
            }
        }
    }
</script>

<style scoped>
    .menu {
        margin: 0 auto;
        background: #2a2a2a;
        display: flex;
        flex: 0 0 auto;
        width: 100%;
    }
</style>