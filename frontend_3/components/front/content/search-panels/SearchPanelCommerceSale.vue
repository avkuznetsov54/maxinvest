<template>
  <Form ref="form" :model="form">
    <div>
      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <div class="form-input-wrap">
            <div class="desktop-filter-titles">
              <span>Тип недвижимости</span>
            </div>
            <FormItem prop="typeComEstate">
              <Select
                v-model="form.typeComEstate"
                multiple
                size="large"
                :max-tag-count="maxTagCount"
                :max-tag-placeholder="more"
              >
                <Option
                  v-for="item in valueFilters.type_commercial_estate"
                  :key="item.id"
                  :value="item.name"
                  >{{ item.name }}</Option
                >
              </Select>
            </FormItem>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <div class="form-input-wrap">
            <div class="desktop-filter-titles">
              <span>Стоимость, руб.</span>
            </div>
            <FormItem>
              <div class="form-input-field">
                <FormItem prop="minCost">
                  <Input
                    v-model="form.minCost"
                    placeholder="От"
                    :maxlength="14"
                    size="large"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxCost">
                  <Input
                    v-model="form.maxCost"
                    placeholder="До"
                    :maxlength="14"
                    size="large"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </FormItem>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="4">
          <div class="form-input-wrap">
            <div class="desktop-filter-titles">
              <span>Площадь, кв.м.</span>
            </div>
            <FormItem>
              <div class="form-input-field">
                <FormItem prop="minSquare">
                  <Input
                    v-model="form.minSquare"
                    placeholder="От"
                    :maxlength="10"
                    size="large"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxSquare">
                  <Input
                    v-model="form.maxSquare"
                    placeholder="До"
                    :maxlength="10"
                    size="large"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </FormItem>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <div class="form-input-wrap">
            <div class="desktop-filter-titles">
              <span>Категория бизнеса</span>
              <Tooltip placement="top" content="Описание что это такое.">
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </div>
            <FormItem prop="businessCategory">
              <Select
                v-model="form.businessCategory"
                multiple
                size="large"
                :max-tag-count="maxTagCount"
                :max-tag-placeholder="more"
              >
                <Option
                  v-for="item in valueFilters.business_category"
                  :key="item.id"
                  :value="item.name"
                  >{{ item.name }}</Option
                >
              </Select>
            </FormItem>
          </div>
        </i-col>
      </Row>
      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <div class="form-input-wrap">
            <FormItem prop="changeCities">
              <Select
                v-model="form.changeCities"
                multiple
                size="large"
                :max-tag-count="maxTagCount"
                class="min-text"
                :max-tag-placeholder="more"
                placeholder="Город"
              >
                <Option
                  v-for="item in cityList"
                  :key="item.value"
                  :value="item.value"
                  >{{ item.label }}</Option
                >
              </Select>
            </FormItem>
          </div>
        </i-col>

        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <div class="form-input-wrap">
            <FormItem prop="changeDistrict">
              <Select
                v-model="form.changeDistrict"
                multiple
                size="large"
                :max-tag-count="maxTagCount"
                :max-tag-placeholder="more"
                placeholder="Район"
              >
                <Option
                  v-for="item in districtList"
                  :key="item.value"
                  :value="item.value"
                  >{{ item.label }}</Option
                >
              </Select>
            </FormItem>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <div class="form-input-wrap">
            <FormItem prop="changeStreet">
              <Select
                v-model="form.changeStreet"
                multiple
                size="large"
                filterable
                :max-tag-count="maxTagCount"
                :max-tag-placeholder="more"
                placeholder="Улица"
              >
                <Option
                  v-for="item in streetList"
                  :key="item.value"
                  :value="item.value"
                  >{{ item.label }}</Option
                >
              </Select>
            </FormItem>
          </div>
        </i-col>

        <i-col :xs="24" :sm="8" :md="6" :lg="4">
          <div class="form-input-wrap">
            <Button size="large" long @click="showExtendedFilter">
              Ещё фильтры
              <Icon
                :type="isExtendedFilter ? 'ios-arrow-down' : 'ios-arrow-up'"
              />
              <!--            <Icon type="ios-arrow-down" />-->
              <!--            <Icon type="ios-arrow-up" />-->
            </Button>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <Button size="large" long type="success" @click="handleSubmit('form')"
            ><b>Показать</b></Button
          >
        </i-col>
      </Row>
      <Row>
        <Button
          size="small"
          :style="{ float: 'right' }"
          @click="handleReset('form')"
        >
          <Icon type="md-trash" />
          Очистить всё
        </Button>
      </Row>
    </div>
    <div
      class="desktop-extended-filter-modal-block"
      :class="{ hidden: isExtendedFilter }"
    >
      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Стоимость за м2</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>

        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <div class="form-input-wrap-extended-filter">
            <FormItem prop="rentCheck">
              <Checkbox v-model="form.rentCheck" size="default"
                >Возможность арендовать
              </Checkbox>
              <Tooltip placement="top" content="Описание что это такое.">
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </FormItem>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <div class="form-input-wrap-extended-filter">
            <FormItem prop="rentCheck">
              <Checkbox v-model="form.rentCheck" size="default"
                >В процессе строительства
              </Checkbox>
              <Tooltip placement="top" content="Описание что это такое.">
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </FormItem>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="4">
          <div class="form-input-wrap-extended-filter">
            <FormItem prop="rentCheck">
              <Checkbox v-model="form.rentCheck" size="default"
                >Готовое
              </Checkbox>
              <Tooltip placement="top" content="Описание что это такое.">
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </FormItem>
          </div>
        </i-col>
      </Row>

      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Этаж</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>

        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Этажность</span>
              <Tooltip placement="top" content="Описание что это такое.">
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>

        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <FormItem prop="rentCheck">
              <Checkbox v-model="form.rentCheck" size="default"
                >Помещение с несколькими этажами</Checkbox
              >
            </FormItem>
          </div>
        </i-col>
      </Row>
      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Возможный доход в<br />месяц</span>
              <Tooltip placement="top" content="Описание что это такое.">
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>

        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Окупаемость</span>
              <Tooltip placement="top" content="Описание что это такое.">
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>

        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Средняя арендная<br />ставка</span>
              <Tooltip
                placement="top"
                content="При сдаче в аренду после покупки."
              >
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>
      </Row>
      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Расположение, линия</span>
              <Tooltip placement="top" content="Описание что это такое.">
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </div>
            <div class="form-input-field">
              <FormItem prop="changeCities">
                <Select
                  v-model="form.changeCities"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in cityList"
                    :key="item.value"
                    :value="item.value"
                    >{{ item.label }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Станция метро</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="changeCities">
                <Select
                  v-model="form.changeCities"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in cityList"
                    :key="item.value"
                    :value="item.value"
                    >{{ item.label }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Расстояние до<br />метро, м.</span>
              <Tooltip placement="top" content="Текст что это такое.">
                <Icon type="md-help" class="icon-class" />
              </Tooltip>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>
      </Row>
      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Отделка</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="changeCities">
                <Select
                  v-model="form.changeCities"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in cityList"
                    :key="item.value"
                    :value="item.value"
                    >{{ item.label }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Системы коммуникаций</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="changeCities">
                <Select
                  v-model="form.changeCities"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in cityList"
                    :key="item.value"
                    :value="item.value"
                    >{{ item.label }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Вытяжка</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="changeCities">
                <Select
                  v-model="form.changeCities"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in cityList"
                    :key="item.value"
                    :value="item.value"
                    >{{ item.label }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </div>
        </i-col>
      </Row>
      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Мощность, кВт</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Высота потолков, м.</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Вход</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="changeCities">
                <Select
                  v-model="form.changeCities"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in cityList"
                    :key="item.value"
                    :value="item.value"
                    >{{ item.label }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </div>
        </i-col>
      </Row>
      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Год постройки</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="4"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="4"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Количество парковок</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="minSquare">
                <Input
                  v-model="form.minSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxSquare">
                <Input
                  v-model="form.maxSquare"
                  placeholder="До"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>
      </Row>

      <Row>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Жилой комплекс</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="changeResComplex">
                <Select
                  v-model="form.changeResComplex"
                  multiple
                  size="large"
                  filterable
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in resComplexList"
                    :key="item.value"
                    :value="item.value"
                    >{{ item.label }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </div>
        </i-col>
        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <div class="form-input-title">
              <span>Класс жилого<br />комплекса</span>
            </div>
            <div class="form-input-field">
              <FormItem prop="changeCities">
                <Select
                  v-model="form.changeCities"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in cityList"
                    :key="item.value"
                    :value="item.value"
                    >{{ item.label }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </div>
        </i-col>
      </Row>
    </div>
  </Form>
</template>

<script>
export default {
  name: 'SearchPanelCommerceSale',

  data() {
    return {
      maxTagCount: 0,
      maxTagCountOne: 1,
      maxTagCountDistrict: 1,

      isExtendedFilter: true,
      anyFilters: 'ios-arrow-down',

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
      streetList: [
        {
          value: 'Большевистская>',
          label: 'Большевистская'
        },
        {
          value: 'Димитрова пр-т',
          label: 'Димитрова пр-т'
        },
        {
          value: 'Родникова 1-я',
          label: 'Родникова 1-я'
        },
        {
          value: 'Днепрогэсовская',
          label: 'Днепрогэсовская'
        }
      ],
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
      catBusinessList: [
        {
          value: 'Общепит',
          label: 'Общепит'
        },
        {
          value: 'Красота',
          label: 'Красота'
        },
        {
          value: 'Здоровье',
          label: 'Здоровье'
        },
        {
          value: 'Услуги',
          label: 'Услуги'
        },
        {
          value: 'Офис',
          label: 'Офис'
        },
        {
          value: 'Производство',
          label: 'Производство'
        }
      ],

      form: {
        typeComEstate: [],
        minCost: '',
        maxCost: '',
        minSquare: '',
        maxSquare: '',
        businessCategory: [],

        changeCities: [],
        changeDistrict: [],
        changeStreet: [],
        changeResComplex: [],
        saleCheck: true,
        rentCheck: false,
        changePurpose: [],
        changeCatBusiness: []
      }
    }
  },
  computed: {
    valueFilters() {
      return this.$store.getters['value-for-filters/GET_VALUE_FILTERS']
    }
  },
  watch: {
    'form.minCost': {
      handler(newValue) {
        this.form.minCost = this.thousandSeparator(newValue)
      }
    },
    'form.maxCost': {
      handler(newValue) {
        this.form.maxCost = this.thousandSeparator(newValue)
      }
    },
    'form.minSquare': {
      handler(newValue) {
        this.form.minSquare = this.thousandSeparator(newValue)
      }
    },
    'form.maxSquare': {
      handler(newValue) {
        this.form.maxSquare = this.thousandSeparator(newValue)
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
    },
    handleReset(name) {
      this.$refs[name].resetFields()
    },
    handleSubmit(name) {
      // eslint-disable-next-line no-console
      console.log(name)
    },
    showExtendedFilter() {
      this.isExtendedFilter = !this.isExtendedFilter
    },
    onlyNumber($event) {
      // console.log($event.keyCode); //keyCodes value
      const keyCode = $event.keyCode ? $event.keyCode : $event.which
      if ((keyCode < 48 || keyCode > 57) && keyCode !== 46) {
        // 46 is dot
        $event.preventDefault()
      }
    },
    more(num) {
      return 'Выбрано: ' + num
    }
  }
}
</script>

<style lang="scss" scoped>
.form-input-wrap {
  margin-bottom: 24px;
}
.desktop-filter-titles {
  margin-bottom: 10px;
  font-weight: 500;
}
.active-check-button {
  color: #fff;
  background-color: #2d8cf0;
  border-color: #2d8cf0;
  &:hover {
    background-color: #57a3f3;
    border-color: #57a3f3;
  }
}
.ivu-form-item {
  width: 100%;
  margin-bottom: 0 !important;
}
.form-input-field {
  display: flex;
}
.desktop-extended-filter-modal-block {
  position: absolute !important;
  max-width: 100%;
  width: 100%;
  /*margin: -5px auto 0px !important;*/
  padding: 30px 20px 0;
  /*border-top: 1px solid #dcdee2;*/
  /*border-radius: 4px;*/
  background-color: #fff;
  /*box-shadow: 0px 16px 38px rgba(0, 0, 0, 0.12);*/
  margin-left: -15px;

  .form-input-field {
    width: 60%;
  }
}
.icon-class {
  border: 1px solid #c5c5c5;
  border-radius: 10px;
  color: #c5c5c5;
}
.form-input-wrap-extended-filter {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}
</style>
