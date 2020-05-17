<template>
  <!--
  <Row>
    <i-col :xs="24" :sm="8" :md="6" :lg="5">
      <div class="desktop-filter-titles">
        <span>Город</span>
      </div>
      <div>
        <Select
          v-model="changeCities"
          multiple
          :max-tag-count="maxTagCountCities"
        >
          <Option
            v-for="item in cityList"
            :key="item.value"
            :value="item.value"
            >{{ item.label }}</Option
          >
        </Select>
      </div>
    </i-col>
    <i-col :xs="24" :sm="8" :md="6" :lg="5">
      <div class="desktop-filter-titles">
        <span>Стоимость, руб.</span>
      </div>
      <div>
        <Input v-model="minCost" placeholder="От" clearable />
        <Input v-model="maxCost" placeholder="До" clearable />
      </div>
    </i-col>
    <i-col :xs="24" :sm="8" :md="6" :lg="5">
      <div class="desktop-filter-titles">
        <span>Площадь, кв.м.</span>
      </div>
      <div>
        <Input v-model="minSquare" placeholder="От" clearable />
        <Input v-model="maxSquare" placeholder="До" clearable />
      </div>
    </i-col>
    <i-col :xs="24" :sm="8" :md="6" :lg="4">
      <div class="desktop-filter-titles">
        <span>Район</span>
      </div>
      <div>
        <Select v-model="changeDistrict" multiple>
          <Option
            v-for="item in districtList"
            :key="item.value"
            :value="item.value"
            >{{ item.label }}</Option
          >
        </Select>
      </div>
    </i-col>
    <i-col :xs="24" :sm="8" :md="6" :lg="4">
      <div class="desktop-filter-titles">
        <span>Жилой комплекс</span>
      </div>
      <div>
        <Select
          v-model="changeResComplex"
          multiple
          filterable
          :max-tag-count="maxTagCount"
        >
          <Option
            v-for="item in resComplexList"
            :key="item.value"
            :value="item.value"
            >{{ item.label }}</Option
          >
        </Select>
      </div>
    </i-col>
  </Row>
  -->
  <Row>
    <Form :model="formTop" label-position="top">
      <i-col :xs="24" :sm="8" :md="6" :lg="5">
        <FormItem label="Город">
          <Select
            v-model="changeCities"
            multiple
            :max-tag-count="maxTagCountCities"
          >
            <Option
              v-for="item in cityList"
              :key="item.value"
              :value="item.value"
              >{{ item.label }}</Option
            >
          </Select>
        </FormItem>
      </i-col>
      <i-col :xs="24" :sm="8" :md="6" :lg="5">
        <FormItem label="Стоимость, руб.">
          <div>
            <Input v-model="minCost" placeholder="От" clearable />
            <Input v-model="maxCost" placeholder="До" clearable />
          </div>
        </FormItem>
      </i-col>
      <i-col :xs="24" :sm="8" :md="6" :lg="5">
        <FormItem label="Площадь, кв.м.">
          <div>
            <Input v-model="minSquare" placeholder="От" clearable />
            <Input v-model="maxSquare" placeholder="До" clearable />
          </div>
        </FormItem>
      </i-col>
      <i-col :xs="24" :sm="8" :md="6" :lg="5">
        <FormItem label="Район">
          <Select
            v-model="changeDistrict"
            multiple
            :max-tag-count="maxTagCountDistrict"
          >
            <Option
              v-for="item in districtList"
              :key="item.value"
              :value="item.value"
              >{{ item.label }}</Option
            >
          </Select>
        </FormItem>
      </i-col>
      <i-col :xs="24" :sm="8" :md="6" :lg="4">
        <FormItem label="Жилой комплекс">
          <Select
            v-model="changeResComplex"
            multiple
            filterable
            :max-tag-count="maxTagCount"
          >
            <Option
              v-for="item in resComplexList"
              :key="item.value"
              :value="item.value"
              >{{ item.label }}</Option
            >
          </Select>
        </FormItem>
      </i-col>
    </Form>
  </Row>
</template>

<script>
export default {
  name: 'SearchPanelCommerce',

  data() {
    return {
      maxTagCount: 0,
      maxTagCountCities: 1,
      maxTagCountDistrict: 1,
      cityList: [
        {
          value: 'Новосибирск',
          label: 'Новосибирск'
        },
        {
          value: 'Бердск',
          label: 'Бердск'
        },
        {
          value: 'р.п. Кольцово',
          label: 'р.п. Кольцово'
        },
        {
          value: 'р.п. Краснообск',
          label: 'р.п. Краснообск'
        }
      ],
      changeCities: [],
      minCost: '',
      maxCost: '',
      minSquare: '',
      maxSquare: '',
      districtList: [
        {
          value: 'Дзержинский',
          label: 'Дзержинский'
        },
        {
          value: 'Железнодорожный',
          label: 'Железнодорожный'
        },
        {
          value: 'Заельцовский',
          label: 'Заельцовский'
        },
        {
          value: 'Калининский',
          label: 'Калининский'
        }
      ],
      changeDistrict: [],
      resComplexList: [
        {
          value: 'Ясный Берег',
          label: 'Ясный Берег'
        },
        {
          value: 'Европейский берег',
          label: 'Европейский бере'
        },
        {
          value: 'Академия',
          label: 'Академия'
        },
        {
          value: 'Октябрьский квартал',
          label: 'Октябрьский квартал'
        }
      ],
      changeResComplex: []
    }
  },
  watch: {
    minCost: {
      handler(newValue) {
        this.minCost = this.thousandSeparator(newValue)
      }
    },
    maxCost: {
      handler(newValue) {
        this.maxCost = this.thousandSeparator(newValue)
      }
    }
  },
  methods: {
    change: (value) => {
      // eslint-disable-next-line no-console
      console.log('wwwwwwww')
    },
    thousandSeparator(newValue) {
      const value = newValue
        .replace(/\D/g, '')
        .replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
      // console.log("thousandSeparator => " + v);
      return value
    }
  }
}
</script>

<style lang="scss" scoped>
.desktop-filter-row {
  display: flex !important;
  /*flex-flow: row nowrap !important;*/
  float: none !important;
}
.desktop-filter-titles {
  margin-bottom: 10px;
  font-weight: 500;
}
.ivu-input-wrapper,
.ivu-input-number {
  width: 48% !important;
}
</style>
