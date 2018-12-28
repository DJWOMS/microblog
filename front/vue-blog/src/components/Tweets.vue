<template>
    <div class="main-tweet">
        <!--<div class="row form-twit">-->
        <!--<form action="{% url 'posts' %}" method="post">-->
        <!--<button type="submit" class="btn btn-tweet">-->
        <!--Отправить-->
        <!--</button>-->
        <!--</form>-->
        <!--</div>-->
        <div class="row tweet" v-for="node in tweet">
            <div class="col-12"><p>{{ node.text }}</p></div>
            <div class="col-12"><b>
                <small>
                    {{ node.date }} -
                    <a href="">{{ node.user.username }}</a>
                </small>

            </b></div>
            <div class="col-12">{{ node.like }} -
                <!--{% if user.is_authenticated %}-->
                <!--<i class="fa fa-thumbs-o-up" aria-hidden="true"-->
                <!--onclick="like({{ node.id }})">-->
                <!--</i>-->
                <!--{% else %}-->
                <!--<a href="/accounts/login/" data-toggle="modal" data-target="#loginModal">-->
                <!--<i class="fa fa-thumbs-o-up" aria-hidden="true"></i>-->
                <!--зарегистрируйтесь, поставить оценку-->
                <!--</a>-->
                <!--{% endif %}-->
                <!--{% if user.is_authenticated and node.user != user %}-->
                <!--<button class="btn btn-follow" onclick="follow(node.user.id)">-->
                <!--Follow-->
                <!--</button>-->
                <!--{% endif %}-->
            </div>
            <hr>
        </div>
        <div class="row tweet">
            <div class="col-12">
                Комментарии
                <!--{{ node.get_descendant_count }}-->
                <!--<i class="fa fa-arrow-down" aria-hidden="true"-->
                <!--onclick="openForm({{ node.id }})"></i>-->

                <!--<i class="fa fa-arrow-up"-->
                <!--onclick="closeForm({{ node.id }})">-->
                <!--</i>-->

                <!--<div class="row">-->
                <!--<div class="col-12 comment" id="{{ node.id }}">-->
                <!--{# Комемнтарии комментариев #}-->
                <!--<div class="col-12">-->
                <!--{% if not node.is_leaf_node %}-->
                <!--<ul class="children">-->
                <!--{{ children }}-->
                <!--</ul>-->
                <!--{% endif %}-->
                <!--</div>-->
                <!--{% if user.is_active and node.level < 4 %}-->
                <!--<form action="{% url 'posts' %}" method="post">-->
                <!--{% csrf_token %}-->
                <!--<input type="number" name="id" hidden value="{{ node.id }}">-->
                <!--{{ form.as_p }}-->
                <!--<button type="submit" class="btn btn-tweet">-->
                <!--Комментировать-->
                <!--</button>-->
                <!--</form>-->
                <!--{% endif %}-->
                <!--</div>-->
                <!--</div>-->
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Tweets",
        props: {
            tweet: ''
        }
    }
</script>

<style scoped>
    .main-tweet {
        margin: 0 auto;
        max-width: 700px;
        box-shadow: 0px 2px 20px 1px #cddae2
    }

    .tweet {
        padding: 10px;
        background: #fff;
        border-left: 1px solid #e6ecf0;
        border-right: 1px solid #e6ecf0;
        border-bottom: 1px solid #e6ecf0;
        margin-right: 0;
        margin-left: 0;
    }

    .tweet:hover {
        background: #f5f8fa;
        cursor: pointer;
    }

    .form-twit {
        width: 100%;
        height: auto;
        padding: 15px;
        margin: 15px auto;
        background: #fff;
        /* box-shadow: 1px 1px 16px 1px #cecece; */
    }

    .comment {
        display: none;
    }

    .btn-tweet {
        border-radius: 100px;
        box-shadow: none;
        cursor: pointer;
        font-size: 14px;
        font-weight: bold;
        line-height: 20px;
        padding: 6px 16px;
        position: relative;
        text-align: center;
        white-space: nowrap;
        background: #46D89E;
    }

    .btn-follow {
        padding: 6px 16px;
        border-radius: 100px;
        background: #00acd8;
    }
</style>