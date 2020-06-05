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
              <span>Способ покупки</span>
            </div>
            <FormItem prop="purchaseMethod">
              <Select
                v-model="form.purchaseMethod"
                multiple
                size="large"
                :max-tag-count="maxTagCount"
                :max-tag-placeholder="more"
              >
                <Option
                  v-for="item in valueFilters.purchase_method"
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
                  v-for="item in valueFilters.city"
                  :key="item.id"
                  :value="item.name"
                  >{{ item.name }}</Option
                >
              </Select>
            </FormItem>
          </div>
        </i-col>

        <!--        <i-col :xs="24" :sm="8" :md="6" :lg="5">-->
        <!--          <div class="form-input-wrap">-->
        <!--            <FormItem prop="changeDistrict">-->
        <!--              <Select-->
        <!--                v-model="form.changeDistrict"-->
        <!--                multiple-->
        <!--                size="large"-->
        <!--                :max-tag-count="maxTagCount"-->
        <!--                :max-tag-placeholder="more"-->
        <!--                placeholder="Район"-->
        <!--              >-->
        <!--                <Option-->
        <!--                  v-for="item in valueFilters.district"-->
        <!--                  :key="item.id"-->
        <!--                  :value="item.name"-->
        <!--                  >{{ item.name }}</Option-->
        <!--                >-->
        <!--              </Select>-->
        <!--            </FormItem>-->
        <!--          </div>-->
        <!--        </i-col>-->
        <i-col :xs="24" :sm="8" :md="6" :lg="5">
          <div class="form-input-wrap">
            <client-only>
              <FormItem prop="changeDistrict">
                <Select
                  v-model="form.changeDistrict"
                  multiple
                  filterable
                  size="large"
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  placeholder="Район"
                  label-in-value
                >
                  <OptionGroup
                    v-for="item in valueFilters.city"
                    :key="item.id"
                    :label="item.name"
                  >
                    <Option
                      v-for="itemCh in item.district_city"
                      :key="itemCh.id"
                      :value="itemCh.name"
                      >{{ itemCh.name }}</Option
                    >
                  </OptionGroup>
                </Select>
              </FormItem>
            </client-only>
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
                  v-for="item in valueFilters.street"
                  :key="item.id"
                  :value="item.name"
                  >{{ item.name }}</Option
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
            ><b>Показать {{ countObj }}</b></Button
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
              <FormItem prop="minCostSquare">
                <Input
                  v-model="form.minCostSquare"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxCostSquare">
                <Input
                  v-model="form.maxCostSquare"
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
            <FormItem prop="buildingCommercialEstate">
              <Checkbox v-model="form.buildingCommercialEstate" size="default"
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
            <FormItem prop="finishedCommercialEstate">
              <Checkbox v-model="form.finishedCommercialEstate" size="default"
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
              <FormItem prop="minFloor">
                <Input
                  v-model="form.minFloor"
                  placeholder="От"
                  :maxlength="3"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxFloor">
                <Input
                  v-model="form.maxFloor"
                  placeholder="До"
                  :maxlength="3"
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
              <FormItem prop="minNumberStoreys">
                <Input
                  v-model="form.minNumberStoreys"
                  placeholder="От"
                  :maxlength="3"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxNumberStoreys">
                <Input
                  v-model="form.maxNumberStoreys"
                  placeholder="До"
                  :maxlength="3"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
            </div>
          </div>
        </i-col>

        <i-col :xs="24" :sm="8" :md="6" :lg="8">
          <div class="form-input-wrap-extended-filter">
            <FormItem prop="severalFloors">
              <Checkbox v-model="form.severalFloors" size="default"
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
              <FormItem prop="minPossibleIncome">
                <Input
                  v-model="form.minPossibleIncome"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxPossibleIncome">
                <Input
                  v-model="form.maxPossibleIncome"
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
              <FormItem prop="minPayback">
                <Input
                  v-model="form.minPayback"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxPayback">
                <Input
                  v-model="form.maxPayback"
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
              <FormItem prop="minAverageRentalRate">
                <Input
                  v-model="form.minAverageRentalRate"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxAverageRentalRate">
                <Input
                  v-model="form.maxAverageRentalRate"
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
              <FormItem prop="relativeLocation">
                <Select
                  v-model="form.relativeLocation"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in valueFilters.relative_location"
                    :key="item.id"
                    :value="item.name"
                    >{{ item.name }}</Option
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
              <FormItem prop="metroStations">
                <Select
                  v-model="form.metroStations"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in valueFilters.metro_stations"
                    :key="item.id"
                    :value="item.name"
                    >{{ item.name }}</Option
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
              <FormItem prop="minDistanceToMetro">
                <Input
                  v-model="form.minDistanceToMetro"
                  placeholder="От"
                  :maxlength="4"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxDistanceToMetro">
                <Input
                  v-model="form.maxDistanceToMetro"
                  placeholder="До"
                  :maxlength="4"
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
              <FormItem prop="finishingProperty">
                <Select
                  v-model="form.finishingProperty"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in valueFilters.finishing_property"
                    :key="item.id"
                    :value="item.name"
                    >{{ item.name }}</Option
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
              <FormItem prop="communicationSystems">
                <Select
                  v-model="form.communicationSystems"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in valueFilters.communication_systems"
                    :key="item.id"
                    :value="item.name"
                    >{{ item.name }}</Option
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
              <FormItem prop="cookerHood">
                <Select
                  v-model="form.cookerHood"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in valueFilters.cooker_hood"
                    :key="item.id"
                    :value="item.name"
                    >{{ item.name }}</Option
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
              <FormItem prop="minKw">
                <Input
                  v-model="form.minKw"
                  placeholder="От"
                  :maxlength="5"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxKw">
                <Input
                  v-model="form.maxKw"
                  placeholder="До"
                  :maxlength="5"
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
              <FormItem prop="minCeilingHeight">
                <Input
                  v-model="form.minCeilingHeight"
                  placeholder="От"
                  :maxlength="10"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxCeilingHeight">
                <Input
                  v-model="form.maxCeilingHeight"
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
              <FormItem prop="typeEntrance">
                <Select
                  v-model="form.typeEntrance"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in valueFilters.type_entrance"
                    :key="item.id"
                    :value="item.name"
                    >{{ item.name }}</Option
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
              <FormItem prop="minYearConstruction">
                <Input
                  v-model="form.minYearConstruction"
                  placeholder="От"
                  :maxlength="4"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxYearConstruction">
                <Input
                  v-model="form.maxYearConstruction"
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
              <FormItem prop="minParking">
                <Input
                  v-model="form.minParking"
                  placeholder="От"
                  :maxlength="5"
                  size="large"
                  @keypress.native="onlyNumber"
                />
              </FormItem>
              <FormItem prop="maxParking">
                <Input
                  v-model="form.maxParking"
                  placeholder="До"
                  :maxlength="5"
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
                    v-for="item in valueFilters.residential_complex"
                    :key="item.id"
                    :value="item.name"
                    >{{ item.name }}</Option
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
              <FormItem prop="classOfHousing">
                <Select
                  v-model="form.classOfHousing"
                  multiple
                  size="large"
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                >
                  <Option
                    v-for="item in valueFilters.class_of_housing"
                    :key="item.id"
                    :value="item.name"
                    >{{ item.name }}</Option
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

      form: {
        // saleCheck: true,
        //
        // typeComEstate: [],
        // purchaseMethod: [],
        // minCost: '',
        // maxCost: '',
        // minSquare: '',
        // maxSquare: '',
        // businessCategory: [],
        // changeCities: [],
        // changeDistrict: [],
        // changeStreet: [],
        // minCostSquare: '',
        // maxCostSquare: '',
        // rentCheck: false,
        // buildingCommercialEstate: false,
        // finishedCommercialEstate: false,
        // minFloor: '',
        // maxFloor: '',
        // minNumberStoreys: '',
        // maxNumberStoreys: '',
        // severalFloors: false,
        // minPossibleIncome: '',
        // maxPossibleIncome: '',
        // minPayback: '',
        // maxPayback: '',
        // minAverageRentalRate: '',
        // maxAverageRentalRate: '',
        // relativeLocation: [],
        // metroStations: [],
        // minDistanceToMetro: '',
        // maxDistanceToMetro: '',
        // finishingProperty: [],
        // communicationSystems: [],
        // cookerHood: [],
        // minKw: '',
        // maxKw: '',
        // minCeilingHeight: '',
        // maxCeilingHeight: '',
        // typeEntrance: [],
        // minYearConstruction: '',
        // maxYearConstruction: '',
        // minParking: '',
        // maxParking: '',
        //
        // changeResComplex: [],
        // classOfHousing: []
      }
    }
  },
  computed: {
    valueFilters() {
      return this.$store.getters['commerce/GET_VALUE_FILTERS']
    },
    countObj() {
      return this.$store.getters['commerce/GET_COUNT_OBJ']
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
  async mounted() {
    if (Object.keys(this.$route.query).length !== 0) {
      this.form = { ...this.form, ...this.$route.query }
    }
    if (
      Object.keys(this.$store.getters['commerce/GET_VALUE_FILTERS']).length ===
      0
    ) {
      await this.$store.dispatch('commerce/FETCH_VALUE_FILTERS')
    }
    if (this.$store.getters['commerce/GET_COUNT_OBJ'] == null) {
      await this.$store.dispatch('commerce/FETCH_COUNT_OBJ')
    }
  },
  methods: {
    // async search() {
    //   await this.$store.dispatch('value-for-filters/FETCH_COUNT_OBJ')
    //   // eslint-disable-next-line no-console
    //   console.log('wewew')
    // },
    change: (value) => {
      // eslint-disable-next-line no-console
      console.log('wwwwwwww')
    },
    thousandSeparator(newValue) {
      if (newValue !== undefined) {
        const value = newValue
          .replace(/\D/g, '')
          .replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
        // console.log("thousandSeparator => " + v);
        return value
      }
      return newValue
    },
    handleReset(name) {
      this.$refs[name].resetFields()
      this.form = {}
      // eslint-disable-next-line no-console
      console.log('очистка формы')
    },
    handleSubmit(name) {
      // eslint-disable-next-line no-console
      console.log(this.form)
      if (this.$route.path !== '/commerce') {
        this.$router.push({ path: '/commerce', query: this.form })

        // eslint-disable-next-line no-console
        console.log('переход на /commerce')
      }
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
    },
    changeSelect(e) {
      // this.$Message.success('true')
      // eslint-disable-next-line no-console
      console.log(e)
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
  /*max-width: 100%;*/
  width: 1200px;
  /*margin: -5px auto 0px !important;*/
  padding: 30px 20px 0;
  /*border-top: 1px solid #dcdee2;*/
  /*border-radius: 4px;*/
  background-color: #fff;
  /*box-shadow: 0px 16px 38px rgba(0, 0, 0, 0.12);*/
  margin-left: -15px;
  z-index: 2;

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
