## Denver residential dwelling sales for 2013

The data is called dwellings_denver.

### Description

Attributes of each dwelling with their selling price for homes that sold in Denver in 2013

The source of this data is < https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-real-property-sales-book-2013 >

### Data format

A data frame with columns:

|variable  |class     |description                                              |
|:---------|:---------|:--------------------------------------------------------|
|parcel    |character |The parcel id                                            |
|nbhd      |numeric   |Neigborhood of the home                                  |
|abstrprd  |numeric   |No clue                                                  |
|livearea  |numeric   |Square footage that is liveable                          |
|finbsmnt  |numeric   |Square footage finished in the basement                  |
|basement  |numeric   |Total square footage of the basement                     |
|yrbuilt   |numeric   |Year the home was built                                  |
|condition |character |Condition of the home (6 levels provided)                |
|quality   |character |A letter ratting                                         |
|totunits  |numeric   |How many dwelling units in the building                  |
|stories   |numeric   |The number of stories                                    |
|gartype   |character |Details on the garage type                               |
|nocars    |numeric   |size of the garage in cars                               |
|xtraffic  |logical   |emtpy                                                    |
|floorlvl  |numeric   |Mostly for apartments.  What level the living unit is on |
|numbdrm   |numeric   |Number of bedrooms                                       |
|numbaths  |numeric   |Number of bathrooms                                      |
|arcstyle  |character |Type of home                                             |
|sprice    |numeric   |Selling price                                            |
|deduct    |numeric   |Deduction from the selling price                         |
|netprice  |numeric   |Net price of home                                        |
|tasp      |numeric   |Tax assesed selling price                                |
|smonth    |numeric   |Month sold                                               |
|syear     |numeric   |Year sold                                                |
|qualified |character |Q or U with 66 percent Q                                 |
|status    |character |I or V with over 90 percent I                            |



## Denver residential dwelling sales for 2013

The data is called dwellings_ml.

### Description

Attributes of each dwelling with their selling price in machine learning format

The source of this data is < https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-real-property-sales-book-2013 >

### Data format

A data frame with columns:

|variable                         |class     |description                                   |
|:--------------------------------|:---------|:---------------------------------------------|
|parcel                           |character |The parcel id                                 |
|abstrprd                         |numeric   |No clue                                       |
|livearea                         |numeric   |Square footage that is liveable               |
|finbsmnt                         |numeric   |Square footage finished in the basement       |
|basement                         |numeric   |Total square footage of the basement          |
|yrbuilt                          |numeric   |Year the home was built                       |
|totunits                         |numeric   |How many dwelling units in the building       |
|stories                          |numeric   |The number of stories                         |
|nocars                           |numeric   |size of the garage in cars                    |
|numbdrm                          |numeric   |Number of bedrooms                            |
|numbaths                         |numeric   |Number of bathrooms                           |
|sprice                           |numeric   |Selling price                                 |
|deduct                           |numeric   |Deduction from the selling price              |
|netprice                         |numeric   |Net price of home                             |
|tasp                             |numeric   |Tax assesed selling price                     |
|smonth                           |numeric   |Month sold                                    |
|syear                            |numeric   |Year sold                                     |
|condition_AVG                    |numeric   |0 or 1 to mark building having attriubte as 1 |
|condition_Excel                  |numeric   |0 or 1 to mark building having attriubte as 1 |
|condition_Fair                   |numeric   |0 or 1 to mark building having attriubte as 1 |
|condition_Good                   |numeric   |0 or 1 to mark building having attriubte as 1 |
|condition_VGood                  |numeric   |0 or 1 to mark building having attriubte as 1 |
|quality_A                        |numeric   |0 or 1 to mark building having attriubte as 1 |
|quality_B                        |numeric   |0 or 1 to mark building having attriubte as 1 |
|quality_C                        |numeric   |0 or 1 to mark building having attriubte as 1 |
|quality_D                        |numeric   |0 or 1 to mark building having attriubte as 1 |
|quality_X                        |numeric   |0 or 1 to mark building having attriubte as 1 |
|gartype_Att                      |numeric   |0 or 1 to mark building having attriubte as 1 |
|gartype_Att/Det                  |numeric   |0 or 1 to mark building having attriubte as 1 |
|gartype_CP                       |numeric   |0 or 1 to mark building having attriubte as 1 |
|gartype_Det                      |numeric   |0 or 1 to mark building having attriubte as 1 |
|gartype_None                     |numeric   |0 or 1 to mark building having attriubte as 1 |
|gartype_att/CP                   |numeric   |0 or 1 to mark building having attriubte as 1 |
|gartype_det/CP                   |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_BI-LEVEL                |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_CONVERSIONS             |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_END UNIT                |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_MIDDLE UNIT             |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_ONE AND HALF-STORY      |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_ONE-STORY               |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_SPLIT LEVEL             |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_THREE-STORY             |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_TRI-LEVEL               |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_TRI-LEVEL WITH BASEMENT |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_TWO AND HALF-STORY      |numeric   |0 or 1 to mark building having attriubte as 1 |
|arcstyle_TWO-STORY               |numeric   |0 or 1 to mark building having attriubte as 1 |
|qualified_Q                      |numeric   |0 or 1 to mark building having attriubte as 1 |
|qualified_U                      |numeric   |0 or 1 to mark building having attriubte as 1 |
|status_I                         |numeric   |0 or 1 to mark building having attriubte as 1 |
|status_V                         |numeric   |0 or 1 to mark building having attriubte as 1 |
|before1980                       |numeric   |0 or 1 to mark building having attriubte as 1 |



## One hot encoded neighbordood variable

The data is called dwellings_neighborhoods_ml.

### Description

Neighborhood attributes for homes that sold in Denver in 2013

The source of this data is < https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-real-property-sales-book-2013 >

### Data format

A data frame with columns:

|variable |class     |description       |
|:--------|:---------|:-----------------|
|parcel   |character |The parcel id     |
|nbhd_1   |numeric   |In neighborhood 1 |
|nbhd_2   |numeric   |NA                |
|nbhd_3   |numeric   |NA                |
|nbhd_4   |numeric   |NA                |
|nbhd_5   |numeric   |NA                |
|nbhd_101 |numeric   |NA                |
|nbhd_104 |numeric   |NA                |
|nbhd_105 |numeric   |NA                |
|nbhd_106 |numeric   |NA                |
|nbhd_107 |numeric   |NA                |
|nbhd_108 |numeric   |NA                |
|nbhd_109 |numeric   |NA                |
|nbhd_110 |numeric   |NA                |
|nbhd_111 |numeric   |NA                |
|nbhd_112 |numeric   |NA                |
|nbhd_113 |numeric   |NA                |
|nbhd_114 |numeric   |NA                |
|nbhd_115 |numeric   |NA                |
|nbhd_116 |numeric   |NA                |
|nbhd_117 |numeric   |NA                |
|nbhd_118 |numeric   |NA                |
|nbhd_120 |numeric   |NA                |
|nbhd_121 |numeric   |NA                |
|nbhd_122 |numeric   |NA                |
|nbhd_123 |numeric   |NA                |
|nbhd_124 |numeric   |NA                |
|nbhd_127 |numeric   |NA                |
|nbhd_128 |numeric   |NA                |
|nbhd_129 |numeric   |NA                |
|nbhd_130 |numeric   |NA                |
|nbhd_131 |numeric   |NA                |
|nbhd_132 |numeric   |NA                |
|nbhd_133 |numeric   |NA                |
|nbhd_201 |numeric   |NA                |
|nbhd_202 |numeric   |NA                |
|nbhd_203 |numeric   |NA                |
|nbhd_205 |numeric   |NA                |
|nbhd_206 |numeric   |NA                |
|nbhd_207 |numeric   |NA                |
|nbhd_208 |numeric   |NA                |
|nbhd_210 |numeric   |NA                |
|nbhd_211 |numeric   |NA                |
|nbhd_212 |numeric   |NA                |
|nbhd_213 |numeric   |NA                |
|nbhd_214 |numeric   |NA                |
|nbhd_215 |numeric   |NA                |
|nbhd_216 |numeric   |NA                |
|nbhd_217 |numeric   |NA                |
|nbhd_218 |numeric   |NA                |
|nbhd_219 |numeric   |NA                |
|nbhd_220 |numeric   |NA                |
|nbhd_221 |numeric   |NA                |
|nbhd_222 |numeric   |NA                |
|nbhd_224 |numeric   |NA                |
|nbhd_225 |numeric   |NA                |
|nbhd_226 |numeric   |NA                |
|nbhd_227 |numeric   |NA                |
|nbhd_228 |numeric   |NA                |
|nbhd_229 |numeric   |NA                |
|nbhd_230 |numeric   |NA                |
|nbhd_231 |numeric   |NA                |
|nbhd_232 |numeric   |NA                |
|nbhd_233 |numeric   |NA                |
|nbhd_234 |numeric   |NA                |
|nbhd_235 |numeric   |NA                |
|nbhd_237 |numeric   |NA                |
|nbhd_238 |numeric   |NA                |
|nbhd_239 |numeric   |NA                |
|nbhd_240 |numeric   |NA                |
|nbhd_241 |numeric   |NA                |
|nbhd_242 |numeric   |NA                |
|nbhd_243 |numeric   |NA                |
|nbhd_244 |numeric   |NA                |
|nbhd_245 |numeric   |NA                |
|nbhd_247 |numeric   |NA                |
|nbhd_248 |numeric   |NA                |
|nbhd_249 |numeric   |NA                |
|nbhd_250 |numeric   |NA                |
|nbhd_252 |numeric   |NA                |
|nbhd_253 |numeric   |NA                |
|nbhd_254 |numeric   |NA                |
|nbhd_255 |numeric   |NA                |
|nbhd_256 |numeric   |NA                |
|nbhd_257 |numeric   |NA                |
|nbhd_258 |numeric   |NA                |
|nbhd_259 |numeric   |NA                |
|nbhd_260 |numeric   |NA                |
|nbhd_301 |numeric   |NA                |
|nbhd_302 |numeric   |NA                |
|nbhd_401 |numeric   |NA                |
|nbhd_402 |numeric   |NA                |
|nbhd_403 |numeric   |NA                |
|nbhd_404 |numeric   |NA                |
|nbhd_503 |numeric   |NA                |
|nbhd_504 |numeric   |NA                |
|nbhd_505 |numeric   |NA                |
|nbhd_506 |numeric   |NA                |
|nbhd_507 |numeric   |NA                |
|nbhd_508 |numeric   |NA                |
|nbhd_509 |numeric   |NA                |
|nbhd_510 |numeric   |NA                |
|nbhd_511 |numeric   |NA                |
|nbhd_512 |numeric   |NA                |
|nbhd_513 |numeric   |NA                |
|nbhd_514 |numeric   |NA                |
|nbhd_515 |numeric   |NA                |
|nbhd_517 |numeric   |NA                |
|nbhd_518 |numeric   |NA                |
|nbhd_519 |numeric   |NA                |
|nbhd_520 |numeric   |NA                |
|nbhd_521 |numeric   |NA                |
|nbhd_522 |numeric   |NA                |
|nbhd_523 |numeric   |NA                |
|nbhd_524 |numeric   |NA                |
|nbhd_525 |numeric   |NA                |
|nbhd_526 |numeric   |NA                |
|nbhd_527 |numeric   |NA                |
|nbhd_528 |numeric   |NA                |
|nbhd_529 |numeric   |NA                |
|nbhd_530 |numeric   |NA                |
|nbhd_531 |numeric   |NA                |
|nbhd_532 |numeric   |NA                |
|nbhd_533 |numeric   |NA                |
|nbhd_534 |numeric   |NA                |
|nbhd_535 |numeric   |NA                |
|nbhd_536 |numeric   |NA                |
|nbhd_537 |numeric   |NA                |
|nbhd_538 |numeric   |NA                |
|nbhd_539 |numeric   |NA                |
|nbhd_540 |numeric   |NA                |
|nbhd_541 |numeric   |NA                |
|nbhd_543 |numeric   |NA                |
|nbhd_544 |numeric   |NA                |
|nbhd_545 |numeric   |NA                |
|nbhd_546 |numeric   |NA                |
|nbhd_547 |numeric   |NA                |
|nbhd_548 |numeric   |NA                |
|nbhd_549 |numeric   |NA                |
|nbhd_550 |numeric   |NA                |
|nbhd_551 |numeric   |NA                |
|nbhd_552 |numeric   |NA                |
|nbhd_553 |numeric   |NA                |
|nbhd_555 |numeric   |NA                |
|nbhd_556 |numeric   |NA                |
|nbhd_580 |numeric   |NA                |
|nbhd_581 |numeric   |NA                |
|nbhd_582 |numeric   |NA                |
|nbhd_583 |numeric   |NA                |
|nbhd_584 |numeric   |NA                |
|nbhd_585 |numeric   |NA                |
|nbhd_586 |numeric   |NA                |
|nbhd_587 |numeric   |NA                |
|nbhd_588 |numeric   |NA                |
|nbhd_589 |numeric   |NA                |
|nbhd_590 |numeric   |NA                |
|nbhd_591 |numeric   |NA                |
|nbhd_592 |numeric   |NA                |
|nbhd_593 |numeric   |NA                |
|nbhd_594 |numeric   |NA                |
|nbhd_596 |numeric   |NA                |
|nbhd_597 |numeric   |NA                |
|nbhd_598 |numeric   |NA                |
|nbhd_599 |numeric   |NA                |
|nbhd_601 |numeric   |NA                |
|nbhd_602 |numeric   |NA                |
|nbhd_604 |numeric   |NA                |
|nbhd_605 |numeric   |NA                |
|nbhd_606 |numeric   |NA                |
|nbhd_607 |numeric   |NA                |
|nbhd_611 |numeric   |NA                |
|nbhd_612 |numeric   |NA                |
|nbhd_613 |numeric   |NA                |
|nbhd_614 |numeric   |NA                |
|nbhd_615 |numeric   |NA                |
|nbhd_616 |numeric   |NA                |
|nbhd_617 |numeric   |NA                |
|nbhd_618 |numeric   |NA                |
|nbhd_620 |numeric   |NA                |
|nbhd_621 |numeric   |NA                |
|nbhd_622 |numeric   |NA                |
|nbhd_623 |numeric   |NA                |
|nbhd_624 |numeric   |NA                |
|nbhd_625 |numeric   |NA                |
|nbhd_627 |numeric   |NA                |
|nbhd_628 |numeric   |NA                |
|nbhd_629 |numeric   |NA                |
|nbhd_630 |numeric   |NA                |
|nbhd_631 |numeric   |NA                |
|nbhd_634 |numeric   |NA                |
|nbhd_635 |numeric   |NA                |
|nbhd_636 |numeric   |NA                |
|nbhd_637 |numeric   |NA                |
|nbhd_638 |numeric   |NA                |
|nbhd_639 |numeric   |NA                |
|nbhd_640 |numeric   |NA                |
|nbhd_641 |numeric   |NA                |
|nbhd_642 |numeric   |NA                |
|nbhd_643 |numeric   |NA                |
|nbhd_644 |numeric   |NA                |
|nbhd_645 |numeric   |NA                |
|nbhd_646 |numeric   |NA                |
|nbhd_647 |numeric   |NA                |
|nbhd_648 |numeric   |NA                |
|nbhd_649 |numeric   |NA                |
|nbhd_650 |numeric   |NA                |
|nbhd_651 |numeric   |NA                |
|nbhd_652 |numeric   |NA                |
|nbhd_653 |numeric   |NA                |
|nbhd_654 |numeric   |NA                |
|nbhd_655 |numeric   |NA                |
|nbhd_656 |numeric   |NA                |
|nbhd_657 |numeric   |NA                |
|nbhd_658 |numeric   |NA                |
|nbhd_659 |numeric   |NA                |
|nbhd_660 |numeric   |NA                |
|nbhd_661 |numeric   |NA                |
|nbhd_663 |numeric   |NA                |
|nbhd_664 |numeric   |NA                |
|nbhd_665 |numeric   |NA                |
|nbhd_666 |numeric   |NA                |
|nbhd_667 |numeric   |NA                |
|nbhd_668 |numeric   |NA                |
|nbhd_669 |numeric   |NA                |
|nbhd_670 |numeric   |NA                |
|nbhd_671 |numeric   |NA                |
|nbhd_672 |numeric   |NA                |
|nbhd_673 |numeric   |NA                |
|nbhd_674 |numeric   |NA                |
|nbhd_675 |numeric   |NA                |
|nbhd_676 |numeric   |NA                |
|nbhd_678 |numeric   |NA                |
|nbhd_679 |numeric   |NA                |
|nbhd_680 |numeric   |NA                |
|nbhd_681 |numeric   |NA                |
|nbhd_682 |numeric   |NA                |
|nbhd_683 |numeric   |NA                |
|nbhd_690 |numeric   |NA                |
|nbhd_691 |numeric   |NA                |
|nbhd_692 |numeric   |NA                |
|nbhd_693 |numeric   |NA                |
|nbhd_694 |numeric   |NA                |
|nbhd_695 |numeric   |NA                |
|nbhd_698 |numeric   |NA                |
|nbhd_702 |numeric   |NA                |
|nbhd_703 |numeric   |NA                |
|nbhd_704 |numeric   |NA                |
|nbhd_705 |numeric   |NA                |
|nbhd_706 |numeric   |NA                |
|nbhd_707 |numeric   |NA                |
|nbhd_708 |numeric   |NA                |
|nbhd_709 |numeric   |NA                |
|nbhd_710 |numeric   |NA                |
|nbhd_711 |numeric   |NA                |
|nbhd_712 |numeric   |NA                |
|nbhd_713 |numeric   |NA                |
|nbhd_714 |numeric   |NA                |
|nbhd_715 |numeric   |NA                |
|nbhd_716 |numeric   |NA                |
|nbhd_717 |numeric   |NA                |
|nbhd_718 |numeric   |NA                |
|nbhd_719 |numeric   |NA                |
|nbhd_720 |numeric   |NA                |
|nbhd_801 |numeric   |NA                |
|nbhd_802 |numeric   |NA                |
|nbhd_803 |numeric   |NA                |
|nbhd_804 |numeric   |NA                |
|nbhd_805 |numeric   |NA                |
|nbhd_901 |numeric   |NA                |
|nbhd_902 |numeric   |NA                |
|nbhd_903 |numeric   |NA                |
|nbhd_904 |numeric   |NA                |
|nbhd_905 |numeric   |NA                |
|nbhd_906 |numeric   |NA                |


