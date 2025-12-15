# Spatial Reach of Intermittence: Hydrological and Biological Indicators

**Research Question:** What is the spatial reach of intermittence and which hydrological and biological features show/indicate this?

**Date:** December 2024

**Sources:** Analysis based on literature collection in the IntermittentStreams repository

---

## Executive Summary

This report synthesizes findings from the scientific literature on intermittent rivers and ephemeral streams (IRES) to address the spatial extent of flow intermittence globally and the hydrological and biological features that indicate or predict intermittence. The key finding is that **non-perennial rivers represent 51-60% of global river length**, making them the rule rather than the exception. Multiple validated biological and hydrological indicators exist for detecting and monitoring intermittence.

---

## 1. Introduction

Intermittent rivers and ephemeral streams (IRES) are watercourses that periodically cease to flow. Despite their prevalence, these systems have historically been overlooked in river science, management, and policy. Understanding the spatial extent of intermittence and developing reliable indicators is critical for:

- Accurate global biogeochemical cycling estimates
- Biodiversity conservation planning
- Water resource management
- Climate change impact assessment
- Regulatory protection of waterways

---

## 2. Spatial Reach of Intermittence

### 2.1 Global Prevalence

The most comprehensive global assessment of non-perennial rivers comes from Messager et al. (2021), published in *Nature*. Using a random forest machine learning model trained on 5,615 gauging stations and 113 environmental predictor variables, the study provides the following key findings:

| Metric | Value |
|--------|-------|
| Global river length that ceases flow ≥1 day/year | **51-60%** |
| Global river length that ceases flow ≥1 month/year | **44-53%** |
| World population living near non-perennial rivers | **52%** |
| River reaches analyzed | 6.2 million |
| Total river network mapped | 23.3 million km |

**Key conclusion:** Non-perennial rivers and streams are the rule rather than the exception on Earth.

### 2.2 Distribution Across Climate Zones

Flow intermittence varies dramatically across climate zones, but occurs in ALL climate types:

| Climate Zone | Intermittence (% of network length) |
|-------------|-------------------------------------|
| Extremely hot and arid | 99% |
| Hot and arid | 99% |
| Arctic (Zone 1) | 96% |
| Warm temperate and xeric | 96% |
| Extremely cold and wet (Zone 2) | 96% |
| Extremely hot and xeric | 95% |
| Arctic (Zone 2) | 92% |
| Cool temperate and xeric | 87% |
| Extremely cold and mesic | 83% |
| Extremely cold and wet (Zone 1) | 72% |
| Cold and mesic | 70% |
| Warm temperate and mesic | 63% |
| Hot and dry | 62% |
| Cool temperate and dry | 57% |
| Hot and mesic | 54% |
| Extremely hot and moist | 30% |
| Cool temperate and moist | 29% |
| Cold and wet | 14% |

*Source: Messager et al. (2021), Table 1*

**Critical insight:** Even in the wettest climates (extremely hot and moist), up to 35% of headwater streams are non-perennial, demonstrating that intermittence is not limited to arid regions.

### 2.3 Distribution by Stream Size

Intermittence prevalence increases with decreasing stream size:

| Mean Annual Flow (m³/s) | % Non-perennial |
|------------------------|-----------------|
| 0.01 - 0.1 (extrapolated) | 70% |
| 0.1 - 1.0 | 47% |
| 1.0 - 10 | 35% |
| 10 - 100 | 26% |
| 100 - 1,000 | 9% |
| 1,000 - 10,000 | 1% |
| ≥10,000 | 0% |

*Source: Messager et al. (2021)*

This pattern reflects the dendritic nature of river networks where small headwater streams, which are more prone to intermittence, constitute the majority of total stream length.

### 2.4 Continental and Regional Patterns

**Australia:** 91-95% of rivers are non-perennial, one of the highest proportions globally.

**Europe:** The SMIRES (Science and Management of Intermittent Rivers and Ephemeral Streams) COST Action catalogued 40+ examples of IRES across Europe, demonstrating their presence across diverse hydroclimatic settings (Sauquet et al. 2020).

**Mediterranean regions:** Characterized by predictable seasonal drought patterns with high intermittence prevalence (Bonada et al. 2007; Acuña et al. 2005).

**United States:** Model predictions suggest 51% intermittence (≥1 zero-flow day/year), though national hydrographic datasets report lower values (19-22%), likely due to inconsistent mapping methodologies.

### 2.5 Climate Change Projections

Döll (2012) modeled climate change impacts on flow regimes globally:

- **6.3-7.0%** of global land area projected to experience ecologically relevant flow regime shifts under high emissions scenario (A2)
- **5.4-6.7%** under lower emissions scenario (B2)
- Many rivers will transition from perennial to intermittent (or transitional) flows
- Low flows projected to be more than halved in almost twice the area compared to mean annual runoff changes

---

## 3. Hydrological Features and Indicators

### 3.1 Primary Predictors of Flow Intermittence

Based on machine learning variable importance analysis from Messager et al. (2021), the following factors predict intermittence (ranked by importance):

**For small-to-medium rivers (MAF < 10 m³/s):**
1. Global aridity index (upstream, annual)
2. Global aridity index (catchment, annual)
3. Soil water content (upstream, annual)
4. Soil water content (catchment, annual)
5. Maximum temperature of warmest month (upstream)
6. Specific discharge (upstream, annual)
7. Land surface runoff (catchment, annual)
8. Maximum temperature of warmest month (catchment)
9. Specific discharge (upstream, minimum)
10. Potential natural vegetation classes

**For medium-to-large rivers (MAF ≥ 1 m³/s):**
1. Global aridity index (upstream, annual)
2. Soil water content (upstream, annual)
3. Global aridity index (catchment, annual)
4. Natural discharge (pour point, minimum)
5. Mean temperature of warmest quarter (upstream)
6. Soil water content (catchment, annual)
7. Maximum temperature of warmest month (upstream)
8. Specific discharge (upstream, minimum)
9. Natural discharge (pour point, annual)
10. Specific discharge (upstream, annual)

### 3.2 Flow Regime Characterization Metrics

The hydrology of IRES can be characterized using multiple metrics (Costigan et al. 2017):

**Temporal Metrics:**
- Magnitude of flow events
- Frequency of zero-flow events
- Duration of dry periods
- Timing of flow cessation and resumption
- Rates of change in flow events
- Predictability of seasonal patterns

**Spatial Metrics:**
- Network contraction extent
- Wet-dry mapping patterns
- Longitudinal connectivity fragmentation
- Distance to perennial refugia

### 3.3 Hydrological States

Studies on chalk rivers in England identified four key hydrological states (visualized and quantified over 20 years):

1. **Dry** - No surface water present
2. **Ponded** - Isolated pools without flow connection
3. **Moderate flow** - Connected flowing water
4. **High flow** - Elevated discharge conditions

**Key findings:**
- Groundwater-dominated systems show slower transitioning between states
- Groundwater-dominated systems exhibit less spatial fragmentation
- Seasonal patterns exist in both composition and configuration of states

### 3.4 Controls on Flow Permanence

Costigan et al. (2016) identified three primary control categories at different scales:

**Meteorologic Controls:**
- Precipitation patterns (amount, timing, intensity)
- Evapotranspiration rates
- Snow accumulation and melt dynamics
- Temperature regimes

**Geologic Controls:**
- Bedrock permeability
- Karst features
- Aquifer characteristics
- Groundwater-surface water interactions

**Land Cover Controls:**
- Riparian vegetation cover
- Impervious surface extent
- Agricultural water use
- Urbanization patterns

---

## 4. Biological Features and Indicators

### 4.1 Macroinvertebrate-Based Indices

#### 4.1.1 Biodrought Index

**Development:** Straka et al. (2019), Czech Republic

**Purpose:** Recognize antecedent stream drying based on benthic invertebrate assemblage composition

**Components:**
- Proportion of indicator taxa
- Proportion of taxa with high body flexibility
- Proportion of taxa preferring organic substrates (autumn)
- Total abundance (spring)

**Performance:**
- 92% correct classification of perennial samples
- 96% correct classification of non-perennial samples
- Misidentification rate between intermittent and perennial: 0-6%

**Validation:** Successfully tested across five Central European countries (Austria, Czech Republic, Germany, Hungary, Slovakia) with 335 samples.

#### 4.1.2 DEHLI Index (Drought Effect of Habitat Loss on Invertebrates)

**Development:** United Kingdom

**Purpose:** Track ecological effects of drought development and recovery

**Mechanism:** Assigns weights to taxa based on their association with key stages of channel drying

**Advantages:**
- More sensitive to drought conditions than flow velocity indices (LIFE score)
- Can detect persistent drought effects months to years after flow recovery
- Differentiates between habitat loss and flow velocity-driven responses

**Applications:**
- Monitoring weather-driven drought effects
- Identifying locations requiring river restoration
- Informing abstraction licensing decisions

#### 4.1.3 MIS-Index (Monitoring Intermittent Streams Index)

**Development:** International collaboration

**Purpose:** Assess invertebrate responses across the full spectrum of environmental conditions (flowing, ponded, drying states)

**Innovation:** Includes semi-aquatic and terrestrial invertebrates from marginal habitats, not just fully aquatic taxa

**Advantages:**
- Holistic assessment across aquatic-terrestrial transitions
- Compatible with standard regulatory sampling methods
- Captures community responses to changing habitat composition

#### 4.1.4 Performance Comparison

Burgazzi et al. (2025) tested DEHLI and MIS-index in Italy:

- Both indices distinguished perennial from intermittent sites
- Rheophilic taxa richness metrics showed strongest responses
- DEHLI performed better due to family-level taxonomic resolution
- Regional adaptation recommended for optimal performance

### 4.2 Indicator Taxa

#### 4.2.1 Taxa Indicating Perennial Conditions (Drying-Sensitive)

| Taxon/Group | Notes |
|-------------|-------|
| EPT taxa (Ephemeroptera, Plecoptera, Trichoptera) | Classic indicator group; rheophilic species especially sensitive |
| Gammarus pulex | Amphipod; uses hyporheic refuge during drought |
| Rheophilic specialists | Require flowing water; lost early in drying sequence |

#### 4.2.2 Taxa Indicating Intermittent Conditions (Drying-Tolerant)

| Taxon/Group | Tolerance Level | Notes |
|-------------|-----------------|-------|
| Nemoura | High | Pollution-sensitive but drying-tolerant |
| Corduliidae | Moderate | Dragonfly family |
| Lepidostoma | Partial | Caddisfly genus |
| OCH taxa (Odonata, Coleoptera, Hemiptera) | Variable | Pool-adapted strategies |

#### 4.2.3 Drying Niche Classification

Research on 33 unpolluted streams identified four macroinvertebrate groups based on drying preferences:

1. **Drying-sensitive taxa** - Lost early in drying gradient
2. **Partly tolerant taxa** - Resistant to initial drying
3. **Generalist taxa** - Broad tolerance range
4. **Specialist taxa** - Adapted to dry conditions

### 4.3 Biological Traits Associated with Intermittence

#### 4.3.1 Traits Indicating Intermittent Flow Regimes

| Trait Category | Specific Traits | Association |
|---------------|-----------------|-------------|
| Body morphology | High body flexibility | Non-perennial streams |
| Life history | Short life cycles (<1 year) | Post-drought recovery |
| Dispersal | Strong aerial dispersal | Recovery after drying |
| Resistance | Desiccation-resistant eggs/cysts | Dry phase survival |
| Respiration | Air-breathing capability | Extreme IRES (especially fish) |
| Habitat preference | Pool/lentic preference | Intermittent sites |
| Trophic | Shredding preference | Correlated with drying tolerance |

#### 4.3.2 Traits Indicating Perennial Conditions

| Trait Category | Specific Traits | Association |
|---------------|-----------------|-------------|
| Life history | Long life cycles (≥1 year) | Stable perennial habitats |
| Dispersal | Weak dispersers | Dependent on connectivity |
| Habitat preference | Rheophilic (flow-loving) | Require continuous flow |
| Respiration | Gill-dependent | Require permanent water |

### 4.4 Community-Level Patterns

#### 4.4.1 Diversity Patterns

- **Alpha diversity:** Declines with increasing drying duration (Leigh & Datry 2016)
- **Highest diversity:** Often observed at low water levels as stream contracts (Acuña et al. 2005)
- **Beta diversity:** Convergent and divergent niche-selection processes act in combination

#### 4.4.2 Community Thresholds

Acuña et al. (2005) identified stepped community responses defined by thresholds:

1. **Drying → Cessation of flow:** Major environmental and community changes
2. **Cessation → Dry phase:** Rapid decline in invertebrate density
3. **Dry phase → Flow resumption:** Community composition differs from pre-drying

#### 4.4.3 Substrate-Specific Responses

Drying impacts vary by substrate type:
- **Cobbles and leaves:** Significant density changes with drying
- **Sand:** Less marked changes with drying

### 4.5 Hyporheic Zone Indicators

The hyporheic zone (saturated sediments below the riverbed) serves as a potential refugium and provides additional bioindicators:

**Key Findings:**
- Proportion of benthos in hyporheic zone increases during drought
- Hyporheic assemblage richness varies predictably with surface drying within regions
- Obligate hypogean (underground-dwelling) taxa abundance increases during drying
- Gammarus pulex and other taxa use hyporheic zone as refuge

**Indicator Potential:**
- Hyporheic invertebrates could complement surface water assessments
- Assemblages differ geographically and by climate but respond predictably to drying within regions
- Particularly valuable when surface water is absent

### 4.6 Fish as Indicators

Fish in IRES exhibit specific adaptations (Kerezsy et al. 2017):

**Survival Strategies:**
- Adaptable colonization strategies
- Flexible recruitment strategies
- Air-breathing capability (specialized species)
- Use of refugia (pools, groundwater-fed areas)

**Indicator Value:**
- Presence of IRES-adapted fish species indicates intermittent conditions
- Community composition reflects flow permanence history
- Endemic species particularly vulnerable to regime shifts

### 4.7 Survival Without Desiccation Resistance

A surprising finding from humid continental climates (Pařil et al. 2019):

- **83% of organisms** (belonging to 22 taxa) survived dry phase without producing desiccation-resistance forms
- Survival promoted by high relative air humidity, riparian cover, and short drying duration
- These surviving organisms contributed substantially to rapid community recovery
- Implies biological indicators may need regional calibration

---

## 5. Methodological Considerations

### 5.1 Challenges in Defining Intermittence

**Threshold definitions vary among studies:**
- Single zero-flow day in entire record
- ≥1 zero-flow day per year on average
- ≥5 zero-flow days per year on average
- ≥1 zero-flow month per year

**Recommendation:** The ≥1 zero-flow day per year threshold is widely used and ecologically meaningful.

### 5.2 Monitoring Approaches

**Hydrological Monitoring:**
- Gauging station networks (spatially biased toward large rivers)
- Citizen science observations
- In-situ sensor networks
- Remote sensing (limited for small streams)
- Wet-dry mapping

**Biological Monitoring:**
- Standard benthic macroinvertebrate sampling
- Multi-habitat sampling protocols (including margins)
- Hyporheic sampling
- Emergence trap collections

### 5.3 Model Validation Considerations

Messager et al. (2021) model performance:
- Overall classification accuracy: 90-92%
- Performance decreases in sparsely gauged basins
- Higher uncertainty in climate zone transition areas
- Local-scale predictions require fine-scale data on soil types, lithology, and groundwater dynamics

---

## 6. Implications and Applications

### 6.1 For River Management

- IRES require tailored management approaches distinct from perennial rivers
- Environmental flow assessments must account for intermittence
- Current biomonitoring tools may misclassify IRES ecological status
- Restoration projects should consider natural intermittence patterns

### 6.2 For Conservation

- 52% of world population lives near non-perennial rivers
- IRES support unique biodiversity adapted to wet-dry cycles
- Endemic species in IRES face extinction risk from flow regime changes
- Protection policies often exclude or inadequately cover IRES

### 6.3 For Climate Change Adaptation

- Monitoring tools needed to detect shifts from perennial to intermittent regimes
- Biological indicators can provide early warning of hydrological changes
- Understanding natural intermittence baseline critical for detecting anthropogenic change

### 6.4 For Biogeochemical Research

- IRES contribute significantly to carbon cycling (up to 10% of daily CO₂ emissions from perennial rivers upon rewetting)
- Omitting IRES from global carbon models leads to underestimation
- Nitrogen cycling and other biogeochemical processes also affected

---

## 7. Knowledge Gaps and Research Priorities

### 7.1 Spatial Understanding
- Fine-scale mapping of intermittence in small headwater streams
- Groundwater-surface water interaction dynamics
- Effects of karst geology on intermittence patterns

### 7.2 Temporal Dynamics
- Long-term trends in intermittence under climate change
- Predictability of flow cessation timing
- Recovery trajectories after drought

### 7.3 Biological Indicators
- Regional calibration of indices across biogeographic zones
- Integration of multiple organism groups (invertebrates, fish, algae)
- Development of functional trait-based approaches
- Validation of hyporheic bioindicators

### 7.4 Management Applications
- Environmental flow standards for IRES
- Biomonitoring protocols specific to intermittent systems
- Decision support tools for managers

---

## 8. Conclusions

1. **Intermittence is globally prevalent:** 51-60% of Earth's rivers cease to flow at least one day per year, occurring across all climate zones and continents.

2. **Climate-induced aridity is the primary driver:** Global aridity index, soil water content, and temperature are the strongest predictors of flow intermittence.

3. **Reliable biological indicators exist:** The Biodrought Index, DEHLI, and MIS-Index can classify flow permanence with high accuracy (>90% in validation studies).

4. **Key biological features include:**
   - Community composition shifts (EPT decline, OCH increase)
   - Trait distributions (body flexibility, dispersal ability, desiccation resistance)
   - Hyporheic zone utilization patterns

5. **Regional calibration is important:** Indicator performance varies across biogeographic regions, requiring local validation and adaptation.

6. **A paradigm shift is needed:** River science, policy, and management must move from a perennial-centric view to one that fully integrates flow intermittence as a fundamental characteristic of river networks.

---

## References

### Primary Sources from Repository

1. **Messager, M.L., Lehner, B., Cockburn, C., et al. (2021).** Global prevalence of non-perennial rivers and streams. *Nature*, 594, 391-397.

2. **Datry, T., Larned, S.T., Tockner, K. (2014).** Intermittent rivers: a challenge for freshwater ecology. *BioScience*, 64(3), 229-235.

3. **Straka, M., et al. (2019).** Recognition of stream drying based on benthic macroinvertebrates: A new tool for Central Europe. *Ecological Indicators* (Biodrought Index).

4. **Leigh, C., Datry, T. (2016).** Drying as a primary hydrological determinant of biodiversity in river systems: a broad-scale analysis. *Ecography*, 40, 487-499.

5. **Döll, P., Schmied, H.M. (2012).** How is the impact of climate change on river flow regimes related to the impact on mean annual runoff? A global-scale analysis. *Environmental Research Letters*, 7, 014037.

6. **Costigan, K.H., Jaeger, K.L., Goss, C.W., Fritz, K.M., Goebel, P.C. (2016).** Understanding controls on flow permanence in intermittent rivers to aid ecological research. *Ecohydrology*, 9, 1141-1153.

7. **Costigan, K.H., et al. (2017).** Flow regimes in intermittent rivers and ephemeral streams. In: *Intermittent Rivers and Ephemeral Streams: Ecology and Management* (Datry et al., eds.), Academic Press.

8. **Bonada, N., et al. (2007).** Macroinvertebrate community structure and biological traits related to flow permanence in a Mediterranean river network. *Hydrobiologia*.

9. **Acuña, V., et al. (2005).** The effects of the intensity of seasonal droughts on stream ecosystems. *Journal of the North American Benthological Society*.

10. **Pařil, P., et al. (2019).** An unexpected source of invertebrate community recovery in intermittent streams from a humid continental climate. *Freshwater Biology*.

11. **Sauquet, E., et al. (2020).** Catalogue of European intermittent rivers and ephemeral streams. SMIRES Technical Report.

12. **Stubbington, R., et al. (2019).** Biomonitoring of intermittent rivers and ephemeral streams in Europe. *Science of the Total Environment*.

13. **Burgazzi, G., et al. (2025).** Testing the performance of macroinvertebrate-based indices of intermittence in Italy. *River Research and Applications*.

14. **Fritz, K.M., et al. (2023).** Identifying invertebrate indicators for streamflow duration assessments in forested headwater streams. *Freshwater Science*.

15. **Kerezsy, A., et al. (2017).** Fish in intermittent rivers and ephemeral streams. In: *Intermittent Rivers and Ephemeral Streams* (Datry et al., eds.).

---

*Report generated from literature analysis of the IntermittentStreams repository*
