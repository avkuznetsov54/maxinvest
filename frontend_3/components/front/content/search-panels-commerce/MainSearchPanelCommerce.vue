<template>
  <div>
    <Form ref="form" :model="form" class="form-sale">
      <div>
        <Row class="mb-2">
          <FormItem prop="typeDeal">
            <RadioGroup
              v-model="typeDeal"
              type="button"
              class="select-mode"
              @input="changeForm"
            >
              <Radio label="sale" class="select-mode-radio">Продажа</Radio>
              <Radio label="rent" class="select-mode-radio">Аренда</Radio>
            </RadioGroup>
          </FormItem>
        </Row>
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
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  @input="changeForm"
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
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  @input="changeForm"
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
            <template v-if="typeDeal === 'sale'">
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
                        @keypress.native="onlyNumber"
                        @input="changeForm"
                      />
                    </FormItem>
                    <FormItem prop="maxCost">
                      <Input
                        v-model="form.maxCost"
                        placeholder="До"
                        :maxlength="14"
                        @keypress.native="onlyNumber"
                        @input="changeForm"
                      />
                    </FormItem>
                  </div>
                </FormItem>
              </div>
            </template>
            <template v-else>
              <div class="form-input-wrap">
                <div class="desktop-filter-titles">
                  <span>Стоимость аренды, руб/мес.</span>
                </div>
                <FormItem>
                  <div class="form-input-field">
                    <FormItem prop="minRent">
                      <Input
                        v-model="form.minRent"
                        placeholder="От"
                        :maxlength="14"
                        @keypress.native="onlyNumber"
                        @input="changeForm"
                      />
                    </FormItem>
                    <FormItem prop="maxRent">
                      <Input
                        v-model="form.maxRent"
                        placeholder="До"
                        :maxlength="14"
                        @keypress.native="onlyNumber"
                        @input="changeForm"
                      />
                    </FormItem>
                  </div>
                </FormItem>
              </div>
            </template>
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
                      @keypress.native="onlyNumber"
                      @input="changeForm"
                    />
                  </FormItem>
                  <FormItem prop="maxSquare">
                    <Input
                      v-model="form.maxSquare"
                      placeholder="До"
                      :maxlength="10"
                      @keypress.native="onlyNumber"
                      @input="changeForm"
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
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </div>
              <FormItem prop="businessCategory">
                <Select
                  v-model="form.businessCategory"
                  multiple
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  @input="changeForm"
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
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                  placeholder="Город"
                  @input="changeForm"
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
              <!--              <client-only>-->
              <FormItem prop="changeDistrict">
                <Select
                  v-model="form.changeDistrict"
                  multiple
                  filterable
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  placeholder="Район"
                  @input="changeForm"
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

              <!--              <FormItem prop="changeDistrict">-->
              <!--                <Select-->
              <!--                  v-model="form.changeDistrict"-->
              <!--                  multiple-->
              <!--                  filterable-->
              <!--                  size="large"-->
              <!--                  :max-tag-count="maxTagCount"-->
              <!--                  :max-tag-placeholder="more"-->
              <!--                  placeholder="Район"-->
              <!--                  label-in-value-->
              <!--                  @on-change="changeSelect"-->
              <!--                >-->
              <!--                  <OptionGroup-->
              <!--                    v-for="item in valueFilters.city"-->
              <!--                    :key="item.id"-->
              <!--                    :label="item.name"-->
              <!--                  >-->
              <!--                    <Option-->
              <!--                      v-for="itemCh in item.district_city"-->
              <!--                      :key="itemCh.id"-->
              <!--                      :value="itemCh.name"-->
              <!--                      label="district"-->
              <!--                      >{{ itemCh.name }}-->
              <!--                    </Option>-->
              <!--                  </OptionGroup>-->

              <!--                  <OptionGroup label="Города">-->
              <!--                    <Option-->
              <!--                      v-for="itemCh in valueFilters.city"-->
              <!--                      :key="itemCh.id"-->
              <!--                      :value="itemCh.name"-->
              <!--                      label="city"-->
              <!--                      >{{ itemCh.name }}</Option-->
              <!--                    >-->
              <!--                  </OptionGroup>-->
              <!--                </Select>-->
              <!--              </FormItem>-->
              <!--              </client-only>-->
            </div>
          </i-col>

          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <div class="form-input-wrap">
              <FormItem prop="changeStreet">
                <Select
                  v-model="form.changeStreet"
                  multiple
                  filterable
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  placeholder="Улица"
                  @input="changeForm"
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
              <Button long @click="showExtendedFilter">
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
            <Button long type="success" @click="handleSubmit('form')"
              ><b>Показать {{ countObj }}</b></Button
            >
          </i-col>
        </Row>
        <Row>
          <!--          <i-col :xs="24" :sm="8" :md="6" :lg="21">-->
          <!--            <div class="filter-tag-line">-->
          <!--              <div v-for="(item, key, i) in tagLine" :key="i">-->
          <!--                <template v-if="typeof item === 'string'">-->
          <!--                  <Tag :key="i" :name="key">-->
          <!--                    {{ item }}-->
          <!--                    <Icon type="ios-close" @click="handleClose2(key, item)" />-->
          <!--                  </Tag>-->
          <!--                </template>-->
          <!--                <template v-else-if="typeof item === 'number'">-->
          <!--                  <Tag :key="i" :name="key">-->
          <!--                    {{ item }}-->
          <!--                    <Icon type="ios-close" @click="handleClose2(key, item)" />-->
          <!--                  </Tag>-->
          <!--                </template>-->
          <!--                <template v-else-if="typeof item === 'object'">-->
          <!--                  <Tag v-for="n in item" :key="n" :name="key">-->
          <!--                    {{ n }}-->
          <!--                    <Icon type="ios-close" @click="handleClose2(key, n)" />-->
          <!--                  </Tag>-->
          <!--                </template>-->
          <!--              </div>-->
          <!--            </div>-->
          <!--          </i-col>-->
          <i-col :xs="24" :sm="8" :md="6" :lg="{ span: 3, offset: 21 }">
            <Button
              size="small"
              :style="{ float: 'right' }"
              @click="handleReset('form')"
            >
              <Icon type="md-trash" />
              Очистить всё
            </Button>
          </i-col>
        </Row>
      </div>
      <div
        class="desktop-extended-filter-modal-block"
        :class="{ hidden: isExtendedFilter }"
      >
        <div class="icon-close-extended-filter" @click="showExtendedFilter">
          <Icon type="ios-close" />
        </div>

        <template v-if="typeDeal === 'sale'">
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
                      @keypress.native="onlyNumber"
                      @input="changeForm"
                    />
                  </FormItem>
                  <FormItem prop="maxCostSquare">
                    <Input
                      v-model="form.maxCostSquare"
                      placeholder="До"
                      :maxlength="10"
                      @keypress.native="onlyNumber"
                      @input="changeForm"
                    />
                  </FormItem>
                </div>
              </div>
            </i-col>
            <i-col :xs="24" :sm="8" :md="6" :lg="5">
              <div class="form-input-wrap-extended-filter">
                <FormItem prop="checkRent">
                  <Checkbox
                    v-model="form.checkRent"
                    size="default"
                    @input="changeForm"
                    >Возможность арендовать
                  </Checkbox>
                  <Tooltip placement="top" content="Описание что это такое.">
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </FormItem>
              </div>
            </i-col>
          </Row>
          <Row class="mb-25">
            <i-col :xs="24" :sm="8" :md="6" :lg="8">
              <div class="form-input-wrap-extended-filter">
                <div class="form-input-title">
                  <span>Возможный доход в<br />месяц</span>
                  <Tooltip placement="top" content="Описание что это такое.">
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </div>
                <div class="form-input-field">
                  <FormItem prop="minPossibleIncome">
                    <Input
                      v-model="form.minPossibleIncome"
                      placeholder="От"
                      :maxlength="10"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                  <FormItem prop="maxPossibleIncome">
                    <Input
                      v-model="form.maxPossibleIncome"
                      placeholder="До"
                      :maxlength="10"
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
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </div>
                <div class="form-input-field">
                  <FormItem prop="minPayback">
                    <Input
                      v-model="form.minPayback"
                      placeholder="От"
                      :maxlength="10"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                  <FormItem prop="maxPayback">
                    <Input
                      v-model="form.maxPayback"
                      placeholder="До"
                      :maxlength="10"
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
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </div>
                <div class="form-input-field">
                  <FormItem prop="minAverageRentalRate">
                    <Input
                      v-model="form.minAverageRentalRate"
                      placeholder="От"
                      :maxlength="10"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                  <FormItem prop="maxAverageRentalRate">
                    <Input
                      v-model="form.maxAverageRentalRate"
                      placeholder="До"
                      :maxlength="10"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                </div>
              </div>
            </i-col>
          </Row>
        </template>
        <template v-else>
          <Row>
            <i-col :xs="24" :sm="8" :md="6" :lg="8">
              <div class="form-input-wrap-extended-filter">
                <div class="form-input-title">
                  <span>Стоимость аренды,<br />руб/кв.м.</span>
                </div>
                <div class="form-input-field">
                  <FormItem prop="rent_price_sq_m">
                    <Input
                      v-model="form.min_rent_price_sq_m"
                      placeholder="От"
                      :maxlength="10"
                      @keypress.native="onlyNumber"
                      @input="changeForm"
                    />
                  </FormItem>
                  <FormItem prop="maxCostSquare">
                    <Input
                      v-model="form.max_rent_price_sq_m"
                      placeholder="До"
                      :maxlength="10"
                      @keypress.native="onlyNumber"
                      @input="changeForm"
                    />
                  </FormItem>
                </div>
              </div>
            </i-col>

            <i-col :xs="24" :sm="8" :md="6" :lg="5">
              <div class="form-input-wrap-extended-filter">
                <FormItem prop="checkSale">
                  <Checkbox
                    v-model="form.checkSale"
                    size="default"
                    @input="changeForm"
                    >Возможность продажи
                  </Checkbox>
                  <Tooltip placement="top" content="Описание что это такое.">
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </FormItem>
              </div>
            </i-col>
          </Row>
        </template>

        <Row>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="severalFloors">
                <Checkbox v-model="form.severalFloors" size="default">
                  <!--                <span>Помещение с несколькими этажами</span>-->
                  <span>Помещение имеет несколько этажей</span>
                  <!--                Несколько этажей-->
                </Checkbox>
              </FormItem>
            </div>
          </i-col>

          <i-col :xs="24" :sm="8" :md="6" :lg="3">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="groundFloor">
                <Checkbox v-model="form.groundFloor" size="default"
                  >Цоколь</Checkbox
                >
              </FormItem>
            </div>
          </i-col>

          <i-col :xs="24" :sm="8" :md="6" :lg="3">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="basement">
                <Checkbox v-model="form.basement" size="default"
                  >Подвал</Checkbox
                >
              </FormItem>
            </div>
          </i-col>
        </Row>
        <Row class="mb-25">
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
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxFloor">
                  <Input
                    v-model="form.maxFloor"
                    placeholder="До"
                    :maxlength="3"
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
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </div>
              <div class="form-input-field">
                <FormItem prop="minNumberStoreys">
                  <Input
                    v-model="form.minNumberStoreys"
                    placeholder="От"
                    :maxlength="3"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxNumberStoreys">
                  <Input
                    v-model="form.maxNumberStoreys"
                    placeholder="До"
                    :maxlength="3"
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
                <span>Расположение,<br />линия</span>
                <Tooltip placement="top" content="Описание что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </div>
              <div class="form-input-field">
                <FormItem prop="relativeLocation">
                  <Select
                    v-model="form.relativeLocation"
                    multiple
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
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </div>
              <div class="form-input-field">
                <FormItem prop="minDistanceToMetro">
                  <Input
                    v-model="form.minDistanceToMetro"
                    placeholder="От"
                    :maxlength="4"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxDistanceToMetro">
                  <Input
                    v-model="form.maxDistanceToMetro"
                    placeholder="До"
                    :maxlength="4"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </div>
          </i-col>
        </Row>
        <Row class="mb-25">
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Бизнес центр</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="businessCenter">
                  <Select
                    v-model="form.businessCenter"
                    multiple
                    filterable
                    :max-tag-count="maxTagCount"
                    :max-tag-placeholder="more"
                  >
                    <Option
                      v-for="item in valueFilters.business_center"
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
                <span>Жилой комплекс</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="changeResComplex">
                  <Select
                    v-model="form.changeResComplex"
                    multiple
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

        <Row class="mb-25">
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="buildingCommercialEstate">
                <Checkbox v-model="form.buildingCommercialEstate" size="default"
                  >В процессе строительства
                </Checkbox>
                <Tooltip placement="top" content="Описание что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </FormItem>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="3">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="finishedCommercialEstate">
                <Checkbox v-model="form.finishedCommercialEstate" size="default"
                  >Готовое
                </Checkbox>
                <Tooltip placement="top" content="Описание что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </FormItem>
            </div>
          </i-col>
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
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxYearConstruction">
                  <Input
                    v-model="form.maxYearConstruction"
                    placeholder="До"
                    :maxlength="4"
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
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxKw">
                  <Input
                    v-model="form.maxKw"
                    placeholder="До"
                    :maxlength="5"
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
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxCeilingHeight">
                  <Input
                    v-model="form.maxCeilingHeight"
                    placeholder="До"
                    :maxlength="10"
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
                <span>Количество парковок</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="minParking">
                  <Input
                    v-model="form.minParking"
                    placeholder="От"
                    :maxlength="5"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxParking">
                  <Input
                    v-model="form.maxParking"
                    placeholder="До"
                    :maxlength="5"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </div>
          </i-col>
        </Row>
      </div>
    </Form>
  </div>
</template>

<script>
export default {
  name: 'MainSearchPanel',
  data() {
    return {
      maxTagCount: 0,
      maxTagCountOne: 1,
      maxTagCountDistrict: 1,

      isExtendedFilter: true,
      anyFilters: 'ios-arrow-down',

      typeDeal: 'sale',
      form: { is_sale: true, is_switchForm: 'sale' },
      tagLine: {}
    }
  },

  computed: {
    valueFilters() {
      return this.$store.getters['commerce/GET_VALUE_FILTERS']
    },
    countObj() {
      return this.$store.getters['commerce/GET_COUNT_OBJ']
    },
    paramsFilter() {
      return this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS']
    }
  },
  watch: {
    // typeDeal(newValue) {
    //   // eslint-disable-next-line no-console
    //   // console.log(newValue)
    //   if (newValue === 'rent') {
    //     delete this.form.is_sale
    //     this.form.is_rent = true
    //   } else if (newValue === 'sale') {
    //     delete this.form.is_rent
    //     this.form.is_sale = true
    //   }
    //   // eslint-disable-next-line no-console
    //   // console.log('this.form =>', this.form)
    // },
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
      // если query-параметры есть, то выбираес их в панели фильтров
      const qp = {}
      const query = this.$route.query
      for (const item in query) {
        // преобразуем строку со значением 'true' в Boolean
        if (query[item] === 'true') {
          query[item] = true
          // if (query === 'is_sale') {
          //   this.typeDeal = 'sale'
          // } else if (query === 'is_rent') {
          //   this.typeDeal = 'rent'
          // }
        } else if (query[item] === 'false') {
          continue
        }
        qp[item] = query[item]
      }
      if (query.is_rent) {
        this.typeDeal = 'rent'
        qp.is_rent = true
        qp.is_switchForm = 'rent'
        this.$store.dispatch('commerce/FETCH_SWITCH_SALE_RENT', this.typeDeal)
      } else {
        this.typeDeal = 'sale'
        qp.is_sale = true
        qp.is_switchForm = 'sale'
        this.$store.dispatch('commerce/FETCH_SWITCH_SALE_RENT', this.typeDeal)
      }
      this.$router.push({ query: qp })
      // eslint-disable-next-line no-console
      // console.log(qp)
      this.form = { ...qp }

      if (this.$store.getters['commerce/FETCH_COMMERCE_OBJ'] === null) {
        if (
          Object.keys(this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS'])
            .length === 0
        ) {
          this.fetchCommerceObj(this.form)
        } else {
          this.fetchCommerceObj(this.paramsFilter)
        }
      }
    } else if (Object.keys(this.$route.query).length === 0) {
      // если query-параметры пусты, то получаем из api объекты
      if (this.$store.getters['commerce/FETCH_COMMERCE_OBJ'] == null) {
        await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', {
          is_sale: true,
          is_switchForm: 'sale'
        })
        // eslint-disable-next-line no-console
        console.log('mounted, length === 0')
      }
    }
    if (
      Object.keys(this.$store.getters['commerce/GET_VALUE_FILTERS']).length ===
      0
    ) {
      await this.$store.dispatch('commerce/FETCH_VALUE_FILTERS')
    }
    // if (this.$store.getters['commerce/GET_COMMERCE_OBJ'] === null) {
    //   await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', {
    //     is_sale: true
    //   })
    //   // eslint-disable-next-line no-console
    //   // console.log('mounted, GET_COMMERCE_OBJ === null')
    // }
  },
  methods: {
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
      // this.$refs[name].resetFields()
      // this.form = {}

      // очищаем поля формы кроме если is_sale=true или is_rent=true
      const keys = Object.keys(this.form)
      keys.forEach((key) => {
        if (key === 'is_sale' && this.form.is_sale) {
          this.form = { is_sale: true, is_switchForm: 'sale' }
          this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
        } else if (key === 'is_rent' && this.form.is_rent) {
          this.form = { is_rent: true, is_switchForm: 'rent' }
          this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
        }
      })
      // this.$router.push({ query: this.form })
      // eslint-disable-next-line no-console
      console.log(this.form)

      if (this.$route.path === '/commerce') {
        this.$router.push({ query: this.paramsFilter })
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
    handleSubmit(name) {
      // eslint-disable-next-line no-console
      // console.log(this.paramsFilter)
      // eslint-disable-next-line no-console
      // console.log(this.form)

      if (this.$route.path !== '/commerce') {
        if (
          Object.keys(this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS'])
            .length === 0
        ) {
          this.$router.push({ path: '/commerce', query: this.form })
          this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
        } else {
          this.$router.push({ path: '/commerce', query: this.paramsFilter })
        }
      }
    },
    changeForm(e) {
      this.switchForm(e)

      // отправляем данные из формы в store
      this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)

      // при изменении в панели фильтров делаем запрос к api
      this.fetchCommerceObj(this.paramsFilter)

      if (this.$route.path === '/commerce') {
        this.$router.push({ query: this.form })
        // eslint-disable-next-line no-console
        // console.log(this.$router)
      }

      // eslint-disable-next-line no-console
      // console.log(this.form)
    },
    switchForm(e) {
      // eslint-disable-next-line no-console
      // console.log(e)
      if (e === 'rent') {
        delete this.form.is_sale
        this.form.is_rent = true
        this.form.is_switchForm = 'rent'
        this.$store.dispatch('commerce/FETCH_SWITCH_SALE_RENT', e)

        delete this.form.minCost
        delete this.form.maxCost
        delete this.form.minCostSquare
        delete this.form.maxCostSquare
        delete this.form.checkRent
        delete this.form.minPossibleIncome
        delete this.form.maxPossibleIncome
        delete this.form.minPayback
        delete this.form.maxPayback
        delete this.form.minAverageRentalRate
        delete this.form.maxAverageRentalRate
      } else if (e === 'sale') {
        delete this.form.is_rent
        this.form.is_sale = true
        this.form.is_switchForm = 'sale'
        this.$store.dispatch('commerce/FETCH_SWITCH_SALE_RENT', e)

        delete this.form.minRent
        delete this.form.maxRent
        delete this.form.min_rent_price_sq_m
        delete this.form.max_rent_price_sq_m
        delete this.form.checkSale
      }

      // eslint-disable-next-line no-console
      // console.log('this.form =>', this.form)
    },
    async fetchCommerceObj(params) {
      const searchParams = new URLSearchParams()
      for (const item in params) {
        if (params[item] !== '' && params[item] !== null) {
          searchParams.append(item, params[item])
        }
        // eslint-disable-next-line no-console
        // console.log(this.form[item])
      }
      await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', searchParams)
    },
    handleClose2(key, value) {
      // закрываем tag
      // eslint-disable-next-line no-console
      console.log(key)
      // const index = this.tagLine.indexOf(name)
      // eslint-disable-next-line no-console
      console.log(value)
      // this.tagLine.splice(index, 1)
    }
  }
}
</script>

<style lang="scss" scoped>
.form-sale {
  font-size: 12px;
}
.filter-tag-line {
  display: flex;
}
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
.ivu-checkbox-wrapper {
  font-size: 12px !important;
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
  box-shadow: 0px 16px 38px rgba(0, 0, 0, 0.12);
  margin-left: -15px;
  z-index: 3;
  margin-top: 16px;

  .form-input-field {
    width: 60%;
  }
}
.icon-close-extended-filter {
  font-size: 56px;
  line-height: 8px;
  position: absolute;
  right: 0;
  top: 18px;
  cursor: pointer;

  .ivu-icon.ivu-icon-ios-close {
    line-height: 0;
  }
}
.icon-class {
  /*border: 1px solid #c5c5c5;*/
  /*border-radius: 10px;*/
  color: #7b7b7b;
  font-size: 15px;
}
.form-input-wrap-extended-filter {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}
</style>
