<template>
    <div class="modal fade" id="loginModal">
        <div class="modal-dialog modal-dialog-centered auth-modal">
            <div class="modal-content">
                <!-- Modal Header -->
                <div class="modal-header">
                    <h4 class="modal-title">Вход</h4>
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                </div>

                <!-- Modal body -->
                <div class="modal-body">
                    <input type="text" placeholder="Логин" value="" v-model="user.username">
                    <input type="password" placeholder="Пароль" value="" v-model="user.password">
                    <button type="button" @click="setLogin">Войти</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data(){
            return {
                user: {
                    username: "",
                    password: ""
                }
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: this.$store.getters.get_url_server + 'auth/token/login/',
                    type: "POST",
                    data: {
                        username: this.user.username,
                        password: this.user.password
                    },
                    success: (response) => {
                        sessionStorage.setItem("token", response.auth_token)
                        this.$router.push({name: "home"})
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>