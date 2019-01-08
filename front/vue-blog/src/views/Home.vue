<template>
    <div class="home">
        <Tweets :tweet="tweets" @reload="loadTweets"></Tweets>
    </div>
</template>

<script>
    import Tweets from '@/components/Tweets'

    export default {
        name: 'home',
        components: {
            Tweets
        },
        data() {
            return {
                tweets: ""
            }
        },
        created() {
            this.loadTweets()
        },
        methods: {
            loadTweets() {
                $.ajax({
                    url: this.$store.getters.get_url_server + 'api/v1/app/',
                    type: "GET",
                    success: (response) => {
                        this.tweets = response
                    }
                })
            }
        }
    }
</script>
