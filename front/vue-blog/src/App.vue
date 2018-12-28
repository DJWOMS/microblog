<template>
    <div id="app">
        <Menu></Menu>
        <router-view/>
    </div>
</template>

<script>
    import Menu from '@/components/Menu.vue'

    export default {
        name: 'app',
        components: {
            Menu
        }
    }
</script>

<style>
    body {
        background: #e6ecf0;
    }
</style>
