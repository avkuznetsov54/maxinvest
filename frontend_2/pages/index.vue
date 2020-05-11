<template>
  <a-layout>
    <a-layout-header>Header</a-layout-header>
    <a-layout-content>
      <a-row type="flex">
        <a-col :span="6" :order="4">
          1 col-order-4
        </a-col>
        <a-col :span="6" :order="3">
          2 col-order-3
        </a-col>
        <a-col :span="6" :order="2">
          3 col-order-2
        </a-col>
        <a-col :span="6" :order="1">
          4 col-order-1
        </a-col>
      </a-row>
    </a-layout-content>
    <a-layout-footer>Footer</a-layout-footer>
  </a-layout>
</template>

<script>
export default {
  components: {}
}
</script>

<style></style>
