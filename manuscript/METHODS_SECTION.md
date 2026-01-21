# **Methods Section for ERW Viability Manuscript**
## **Enhanced Rock Weathering Potential on São Miguel Island (Azores)**

---

## **2. MATERIALS AND METHODS**

### **2.1 Study Site**

This study was conducted in the Sanguinho agricultural area of São Miguel Island, Azores Archipelago, Portugal (37°78'N, 25°50'W). São Miguel is a volcanic island located in the North Atlantic Ocean, approximately 1,400 km west of mainland Portugal. The island covers 744 km² and has a population of approximately 140,000 inhabitants.

The Sanguinho area is representative of intensive dairy agriculture on São Miguel, with pasture-based systems supporting the island's milk production industry. The region experiences a subtropical oceanic climate (Köppen classification: Cfb) with high annual rainfall (1,500-2,000 mm/yr), mild temperatures (14-22°C), and high humidity (75-85%). These climatic conditions, combined with young volcanic soils derived from Quaternary basalt flows, provide ideal conditions for grass growth and potentially for enhanced rock weathering.

The study area comprises 11 agricultural plots (total area: 22 hectares) managed by local dairy farmer João Moleiro. All plots are actively managed for dairy cattle grazing, with current agricultural practices including annual application of dolomitic lime (3,000-5,000 kg/ha) for pH correction and magnesium supplementation.

---

### **2.2 Soil Sampling and Analysis**

#### **2.2.1 Sample Collection**

Soil samples were collected from 11 agricultural plots in the Sanguinho area during the 2024 growing season. Sampling was conducted by Terra Verde Agricultural Association, a certified agronomic service provider in the Azores, following standard Portuguese protocols for agricultural soil analysis (Laboratório Químico Agrícola Rebelo da Silva methods).

At each plot, composite soil samples were collected from the 0-20 cm depth using a systematic grid approach (minimum 15 subsamples per plot). Samples were air-dried, sieved to <2 mm, and submitted for analysis at an ISO 17025-accredited laboratory.

#### **2.2.2 Soil Chemical Analysis**

The following parameters were measured using standard agronomic methods:

**pH:** Measured in 1:2.5 soil:water suspension using a glass electrode (LQARS method 1.1).

**Organic Matter:** Determined by the Walkley-Black wet oxidation method (LQARS method 3.1).

**Exchangeable Cations (Ca²⁺, Mg²⁺, K⁺):** Extracted with 1 M ammonium acetate (pH 7.0) and quantified by atomic absorption spectroscopy (AAS) or inductively coupled plasma optical emission spectrometry (ICP-OES) (LQARS method 4.1).

**Cation Exchange Capacity (CEC):** Calculated as the sum of exchangeable cations plus exchangeable acidity (LQARS method 4.2).

**Base Saturation:** Calculated as (sum of exchangeable bases / CEC) × 100%.

**Extractable Phosphorus and Potassium:** Determined by the Egner-Riehm method (ammonium lactate-acetic acid extraction) followed by colorimetric (P) or flame photometric (K) determination (LQARS methods 5.1 and 5.2).

All analyses were performed in triplicate, with quality control samples (blanks, certified reference materials, and duplicate analyses) run at a frequency of 10% of total samples.

---

### **2.3 Weathering Rate Estimation**

#### **2.3.1 Conceptual Model**

Enhanced rock weathering CO₂ removal rates were estimated using a multi-factor weathering model that accounts for soil chemistry, climate, and basalt composition. The model is based on established geochemical weathering theory and calibrated against published field and laboratory studies (Beerling et al. 2020; Kantola et al. 2017; Kelland et al. 2020).

The general form of the weathering rate model is:

$$
R_{\text{weather}} = R_{\text{base}} \times f(pH) \times f(OM) \times f(climate) \times f(basalt)
$$

where:
- $R_{\text{base}}$ = baseline weathering rate (neutral pH, low OM, temperate climate)
- $f(pH)$ = pH effect multiplier
- $f(OM)$ = organic matter effect multiplier
- $f(climate)$ = climate effect multiplier (rainfall and temperature)
- $f(basalt)$ = basalt composition effect

#### **2.3.2 pH Effect on Weathering Rate**

Mineral dissolution kinetics are strongly pH-dependent, with dissolution rates increasing exponentially at lower pH values (White & Brantley 2003; Gislason & Oelkers 2003). The pH effect was modeled using a simplified rate law:

$$
f(pH) = 10^{(7-pH)} / 10^{(7-7)}
$$

This formulation is consistent with transition state theory for silicate mineral dissolution under acidic conditions, where proton-promoted dissolution dominates (Lasaga 1981). The exponent was normalized to provide a multiplier of 1.0 at pH 7.0 (neutral baseline).

For the pH range observed in this study (5.2-6.0), this equation predicts weathering rate enhancements of 10-63x relative to neutral pH. However, to account for field-scale limitations (mineral surface area reduction over time, diffusion limitations, secondary mineral precipitation), we applied a scaling factor (exponent = 0.3) to provide more conservative estimates:

$$
f(pH)_{\text{field}} = \left(10^{(7-pH)}\right)^{0.3}
$$

#### **2.3.3 Organic Matter Effect**

High organic matter content enhances weathering through multiple mechanisms:
1. Organic acid production (oxalic, citric, malic acids) that chelates cations and lowers local pH at mineral surfaces
2. Elevated soil CO₂ concentrations (10-100x atmospheric) from microbial respiration
3. Enhanced microbial weathering (fungal hyphae, bacterial biofilms)
4. Increased water retention, prolonging mineral-water contact time

The organic matter effect was modeled as a linear enhancement:

$$
f(OM) = 1.0 + (OM\% - 2.0) \times 0.15
$$

where OM% is the soil organic matter percentage, and 2.0% represents a low-OM baseline. This parameterization is based on observed weathering rate differences between high-OM agricultural soils and low-OM mineral soils in previous ERW studies (Kelland et al. 2020; Haque et al. 2020).

#### **2.3.4 Climate Effect**

Climate influences weathering rates through both rainfall (water availability for dissolution) and temperature (kinetic energy for mineral reactions). The climate effect was modeled as:

$$
f(climate) = \left(\frac{P}{1000}\right) \times \exp\left(\frac{-E_a}{R}\left(\frac{1}{T} - \frac{1}{285}\right)\right)
$$

where:
- $P$ = annual precipitation (mm)
- $E_a$ = apparent activation energy (assumed 50 kJ/mol for field-scale weathering)
- $R$ = gas constant (8.314 J/mol·K)
- $T$ = mean annual temperature (K)
- 285 K (12°C) = temperate baseline temperature

For São Miguel (P = 1,750 mm/yr, T = 291 K [18°C]), this yields a climate multiplier of approximately 2.5x relative to a temperate baseline (P = 1,000 mm/yr, T = 285 K).

To provide conservative field-scale estimates, we applied a square-root scaling factor:

$$
f(climate)_{\text{field}} = \sqrt{\left(\frac{P}{1000}\right) \times 1.2}
$$

where the 1.2 factor accounts for the temperature effect at 18°C.

#### **2.3.5 Basalt Composition**

Basalt composition affects weathering rates through the abundance of rapidly weathering minerals (olivine, pyroxene) and the availability of Mg²⁺ and Ca²⁺ for CO₂ sequestration. Based on typical São Miguel basalt composition (assumed MgO = 8%, CaO = 10%; Moore 1990; Guest et al. 1999), we calculated the theoretical CO₂ sequestration potential from the weathering reactions:

$$
\text{MgO} + \text{CO}_2 \rightarrow \text{MgCO}_3
$$
$$
\text{CaO} + \text{CO}_2 \rightarrow \text{CaCO}_3
$$

The stoichiometric CO₂ sequestration was calculated as:

$$
\text{CO}_2 \text{ (kg)} = \left(\text{MgO (kg)} \times \frac{44}{40}\right) + \left(\text{CaO (kg)} \times \frac{44}{56}\right)
$$

where 44, 40, and 56 are the molecular weights of CO₂, MgO, and CaO, respectively.

A weathering efficiency factor of 0.45 (45% dissolution over 10 years) was applied to account for incomplete weathering in agricultural timescales. This value is consistent with field trials showing 30-60% dissolution of fine basalt powder (<100 μm) in agricultural soils over 5-10 years (Kelland et al. 2020; Amann et al. 2022).

---

### **2.4 Application Scenarios**

Two ERW implementation scenarios were modeled:

#### **2.4.1 Lime Replacement Scenario (Conservative)**

This scenario assumes basalt application at rates equivalent to current agricultural lime practice:
- **Application rate:** 2,700 kg basalt/ha/yr (annual)
- **Rationale:** Replaces current dolomitic lime application (3,000 kg/ha/yr) with locally sourced basalt
- **Target:** pH maintenance and Mg supplementation
- **CO₂ accounting period:** 10 years
- **Expected weathering:** 45% over 10 years (4.5% per year, declining)

#### **2.4.2 Full ERW Scenario (Aggressive)**

This scenario assumes a one-time high-rate basalt application for maximum CDR:
- **Application rate:** 50,000 kg basalt/ha (one-time)
- **Rationale:** Maximize CO₂ removal while maintaining agricultural productivity
- **Target:** Long-term pH buffering and sustained nutrient release
- **CO₂ accounting period:** 10 years
- **Expected weathering:** 45% over 10 years (exponential decay model)

For both scenarios, CO₂ removal rates were calculated for each plot based on plot-specific soil chemistry and the weathering model described in Section 2.3.

---

### **2.5 Economic Analysis**

#### **2.5.1 Cost-Benefit Modeling**

Economic viability was assessed by comparing the total costs and benefits of ERW implementation against current agricultural practice (dolomitic lime application).

**Current Practice Costs:**
- Dolomitic lime: €40/tonne (CIF São Miguel, includes shipping from mainland Portugal)
- Application rate: 3,000 kg/ha/yr
- Annual cost: €120/ha/yr

**ERW Alternative Costs:**
- Basalt (crushed, <1 mm): €13/tonne (ex-quarry, São Miguel)
- Application rate: 2,700 kg/ha/yr (lime replacement) or 50,000 kg/ha (one-time, full ERW)
- Annual cost: €35/ha/yr (lime replacement) or €650/ha amortized over 10 years (€65/ha/yr)

**Benefits:**
1. **Cost savings:** Reduced expenditure on pH amendment (€85/ha/yr for lime replacement)
2. **Carbon credit revenue:** Based on verified CO₂ removal (€80/tCO₂, based on 2024 voluntary carbon market prices for durable CDR)
3. **Co-benefits (not monetized):** Improved soil structure, micronutrient addition (Fe, Mn, Zn), reduced runoff pollution

Total farmer benefit was calculated as:

$$
\text{Benefit (€/ha/yr)} = \text{Cost savings} + \text{Carbon revenue} - \text{Additional costs}
$$

#### **2.5.2 Scaling Analysis**

Island-scale economic potential was estimated by extrapolating pilot-scale results to the total suitable agricultural area on São Miguel (~15,000 ha of dairy pasture with acidic soils, pH <6.5). Adoption scenarios ranged from 10% (1,500 ha) to 50% (7,500 ha) of suitable land area. This analysis accounted for:
- Basalt supply constraints (assumed 5-10 quarries, 2,000-5,000 t/yr each)
- Farmer adoption rates (based on agronomic literature and extension program experience)
- Carbon market development (assumes verified MRV protocol and buyer agreements)

---

### **2.6 Viability Scoring System**

To objectively rank plots for pilot project site selection, we developed a multi-criteria viability scoring system (0-100 points) based on factors known to influence ERW effectiveness:

| **Factor** | **Weight** | **Rationale** | **Scoring Function** |
|------------|-----------|---------------|----------------------|
| pH | 30% | Primary control on weathering kinetics | pH 5.0=30, pH 7.0=15, pH 8.0=5 (linear interpolation) |
| Organic Matter | 20% | Biological weathering enhancement | 12%=20, 6%=12, 2%=3 (linear) |
| Mg Deficit | 15% | Farmer motivation and nutrient need | -2.0 cmol/kg=15, 0=2 (linear) |
| CEC | 10% | Ion exchange capacity and buffering | 20=10, 10=8, 5=3 (linear) |
| Climate (Rainfall) | 15% | Water availability for dissolution | Fixed at 15 (same for all plots in study area) |
| Climate (Temperature) | 10% | Kinetic energy for reactions | Fixed at 10 (same for all plots in study area) |

Plots with scores ≥90 were classified as "EXCEPTIONAL," 80-89 as "EXCELLENT," 70-79 as "VERY GOOD," 60-69 as "GOOD," 50-59 as "MODERATE," and <50 as "MARGINAL."

The top three plots were selected for pilot project implementation based on:
1. Highest viability scores
2. Diverse pH/OM conditions (to test weathering model sensitivity)
3. Farmer accessibility and willingness to participate

---

### **2.7 Uncertainty Analysis**

Several sources of uncertainty affect the weathering rate estimates and CO₂ removal projections:

1. **Basalt composition:** Assumed typical São Miguel basalt (MgO=8%, CaO=10%). Actual composition will be measured via X-ray fluorescence (XRF) analysis of quarry samples (planned, n=5-10 quarries).

2. **Weathering efficiency:** Assumed 45% dissolution over 10 years based on literature. Field monitoring (planned) will measure actual dissolution rates via soil solution chemistry and alkalinity export.

3. **Secondary mineral precipitation:** CO₂ removal may be partially offset if bicarbonate precipitates as secondary carbonates within the soil profile before export. Soil core analysis (planned) will quantify this effect.

4. **Field-scale heterogeneity:** Composite samples represent plot-average conditions. Within-plot variability (e.g., pH, OM) will be assessed during pilot monitoring.

5. **Climate variability:** Modeled rates assume average rainfall (1,750 mm/yr). Interannual variability (dry vs. wet years) will affect actual rates.

To provide conservative estimates, we applied scaling factors to reduce laboratory-based weathering rates to field-relevant values (pH exponent = 0.3, climate square-root scaling). Final CO₂ removal estimates should be considered preliminary until validated by field monitoring data.

---

### **2.8 Statistical Analysis**

Descriptive statistics (mean, standard deviation, range) were calculated for all soil parameters. Pearson correlation coefficients were computed to assess relationships between soil properties and calculated viability scores. All statistical analyses were performed using Python 3.x with standard libraries (dataclasses, statistics, csv). A significance level of α = 0.05 was used for all tests.

---

### **2.9 Data Availability**

All raw soil analysis data, Python analysis scripts, and viability scoring results are available in the project repository:
- GitHub: https://github.com/[username]/ERW---Volcanic-Islands
- Soil data: `/data/sao_miguel_soil_analysis.md`
- Analysis script: `/scripts/viability_analysis_simple.py`
- Results: `/data/sao_miguel_viability_results.csv`

---

### **2.10 Ethical Considerations**

This study was conducted as an agricultural assessment for ERW feasibility. No human subjects research was conducted. Soil sampling was performed with the informed consent of the landowner (João Moleiro) and coordinated through the Terra Verde Agricultural Association, a trusted local organization. All data have been anonymized (plot identifiers only, no GPS coordinates) to protect farmer privacy.

---

## **References for Methods**

Amann, T., Hartmann, J., Struyf, E., Garcia, W.D., Fischer, E.K., Janssens, I., Meire, P., Schoelynck, J., 2022. Enhanced weathering and related element fluxes - a cropland mesocosm approach. Biogeosciences 19, 103–119.

Beerling, D.J., Kantzas, E.P., Lomas, M.R., Wade, P., Eufrasio, R.M., Renforth, P., Sarkar, B., Andrews, M.G., James, R.H., Pearce, C.R., Mercure, J.-F., Pollitt, H., Holden, P.B., Edwards, N.R., Khanna, M., Koh, L., Quegan, S., Pidgeon, N.F., Janssens, I.A., Hansen, J., Banwart, S.A., 2020. Potential for large-scale CO2 removal via enhanced rock weathering with croplands. Nature 583, 242–248.

Gislason, S.R., Oelkers, E.H., 2003. Mechanism, rates, and consequences of basaltic glass dissolution: II. An experimental study of the dissolution rates of basaltic glass as a function of pH and temperature. Geochimica et Cosmochimica Acta 67, 3817–3832.

Guest, J.E., Gaspar, J.L., Cole, P.D., Queiroz, G., Duncan, A.M., Wallenstein, N., Ferreira, T., Pacheco, J.-M., 1999. Volcanic geology of Furnas Volcano, São Miguel, Azores. Journal of Volcanology and Geothermal Research 92, 1–29.

Haque, F., Santos, R.M., Chiang, Y.W., 2020. CO2 sequestration by wollastonite-amended agricultural soils – An Ontario field study. International Journal of Greenhouse Gas Control 97, 103017.

Kantola, I.B., Masters, M.D., Beerling, D.J., Long, S.P., DeLucia, E.H., 2017. Potential of global croplands and bioenergy crops for climate change mitigation through deployment for enhanced weathering. Biology Letters 13, 20160714.

Kelland, M.E., Wade, P.W., Lewis, A.L., Taylor, L.L., Sarkar, B., Andrews, M.G., Lomas, M.R., Cotton, T.E.A., Kemp, S.J., James, R.H., Pearce, C.R., Hartley, S.E., Hodson, M.E., Leake, J.R., Banwart, S.A., Beerling, D.J., 2020. Increased yield and CO2 sequestration potential with the C4 cereal Sorghum bicolor cultivated in basaltic rock dust-amended agricultural soil. Global Change Biology 26, 3658–3676.

Lasaga, A.C., 1981. Transition state theory. Reviews in Mineralogy 8, 135–169.

Moore, R.B., 1990. Volcanic geology and eruption frequency, São Miguel, Azores. Bulletin of Volcanology 52, 602–614.

White, A.F., Brantley, S.L., 2003. The effect of time on the weathering of silicate minerals: why do weathering rates differ in the laboratory and field? Chemical Geology 202, 479–506.

---

**Methods Section Status:** ✅ COMPLETE  
**Word Count:** ~2,900 words  
**Target Journal:** *Frontiers in Climate*, *Applied Geochemistry*, or *Nature Climate Change*  
**Next Steps:** Results section, Discussion section, Figure preparation
