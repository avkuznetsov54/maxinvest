<template>
  <Menu mode="horizontal" theme="dark" active-name="1">
    <div class="container">
      <MenuItem name="1">
        <!--        <Icon type="ios-paper" />-->
        <nuxt-link to="/novostroyki/" :style="{ color: 'white' }"
          >Новостройки без комиссии</nuxt-link
        >
      </MenuItem>
      <!--      <Submenu name="2">-->
      <!--        <template slot="title">-->
      <!--          &lt;!&ndash;          <Icon type="ios-stats" />&ndash;&gt;-->
      <!--          Коммерческая-->
      <!--        </template>-->
      <!--        <MenuGroup title="Категория бизнеса">-->
      <!--          <MenuItem name="3-1">Категория 1 Категория 1</MenuItem>-->
      <!--          <MenuItem name="3-2">Категория 2</MenuItem>-->
      <!--          <MenuItem name="3-3">Категория 3</MenuItem>-->
      <!--        </MenuGroup>-->
      <!--        <MenuGroup title="留存">-->
      <!--          <MenuItem name="3-4">用户留存</MenuItem>-->
      <!--          <MenuItem name="3-5">流失用户</MenuItem>-->
      <!--        </MenuGroup>-->
      <!--      </Submenu>-->
      <!--      <MenuItem name="3">-->
      <!--        <Icon type="ios-construct" />-->
      <!--        综合设置-->
      <!--      </MenuItem>-->
      <Dropdown
        class="top-line-dropdown"
        trigger="custom"
        :visible="visible"
        style="margin-left: 20px"
      >
        <span @click="handleToggeleOpen">
          Коммерческая
          <Icon type="ios-arrow-down"></Icon>
        </span>
        <!--        <DropdownMenu slot="list" @mouseleave.native="handleClose">-->
        <DropdownMenu slot="list" @mouseleave.native="handleClose">
          <p>Коммерческая в жилых комплексах</p>
          <div style="text-align: right;margin:10px; width: 500px">
            <Button type="primary" @click="handleClose">OK</Button>
          </div>
        </DropdownMenu>
      </Dropdown>
      <MenuItem name="2">
        <!--        <Icon type="ios-paper" />-->
        <nuxt-link to="/" :style="{ color: 'white' }">Ипотека</nuxt-link>
      </MenuItem>
    </div>
  </Menu>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      visible: false
    }
  },
  methods: {
    handleToggeleOpen() {
      this.visible = !this.visible
    },
    handleClose() {
      this.visible = false
    }
  }
}
</script>

<style lang="scss" scoped>
.top-line-dropdown {
  color: #fff;
}
/*a {*/
/*  color: #fff;*/
/*  &: hover {*/
/*    color: #7f828b;*/
/*  }*/
/*}*/
.ivu-menu-horizontal {
  height: 40px;
  line-height: 40px;
}
</style>
