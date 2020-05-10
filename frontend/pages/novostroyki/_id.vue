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
    <footer></footer>
  </article>
</template>

<script>
export default {
  // validate принимает аргумени ctx,
  // который содержит объект params - параметры адресной строки
  validate({ params }) {
    return Boolean(params.id) // если params.id === undefined, то будет false
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
    width: 100%
    height: auto

.object-header
  margin-bottom: 1.5rem
</style>
