<template>
  <article>
    <header class="object-header">
      <div class="object-title">
        <h1>Name Novostroyka</h1>
        <nuxt-link to="/">
          <i class="el-icon-back"></i>
        </nuxt-link>
      </div>
      <div class="object-info">
        <small>
          <i class="el-icon-item"></i>
          {{ new Date().toDateString() }}
        </small>
        <small>
          <i class="el-icon-view"></i>
          42
        </small>
      </div>
      <div class="object-image">
        <img
          src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
          alt="hamburger"
        />
      </div>
    </header>
    <main class="object-text">
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum dolorum
        facilis harum libero magnam, officiis tenetur! Consectetur in quis quos?
        At deleniti hic id nihil, nulla quam quia quos tenetur!
      </p>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum dolorum
        facilis harum libero magnam, officiis tenetur! Consectetur in quis quos?
        At deleniti hic id nihil, nulla quam quia quos tenetur!
      </p>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum dolorum
        facilis harum libero magnam, officiis tenetur! Consectetur in quis quos?
        At deleniti hic id nihil, nulla quam quia quos tenetur!
      </p>
    </main>
    <footer>
      <!--      <app-comment-form-->
      <!--        v-if="canAddComment"-->
      <!--        @created="createCommentHandler"-->
      <!--        :postId="post._id"-->
      <!--      />-->
      <!--      <div class="comments" v-if="post.comments.length">-->
      <!--        <app-comment-->
      <!--          v-for="comment in post.comments"-->
      <!--          :key="comment._id"-->
      <!--          :comment="comment"-->
      <!--        />-->
      <!--      </div>-->
      <!--      <div class="text-center" v-else>Квартир нет</div>-->
      <b-row>
        <b-col v-for="obj in 6" :key="obj" cols="12" sm="6" md="4" lg="3">
          <app-card-residential-premise />
        </b-col>
      </b-row>
    </footer>
  </article>
</template>

<script>
import AppCardResidentialPremise from '@/components/front/main/CardResidentialPremise'
export default {
  // validate принимает аргумени ctx,
  // который содержит объект params - параметры адресной строки
  validate({ params }) {
    return Boolean(params.id) // если params.id === undefined, то будет false
  },
  components: {
    AppCardResidentialPremise
  }
}
</script>

<style lang="sass" scoped>
.object-title
  display: flex
  justify-content: space-between
  align-items: center
  margin-bottom: 1rem

.object-info
  display: flex
  justify-content: space-between
  align-items: center
  margin-bottom: 0.5rem

.object-image
  img
    width: auto
    height: 400px

.object-header
  margin-bottom: 1.5rem
</style>
