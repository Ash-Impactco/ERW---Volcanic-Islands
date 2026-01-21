# São Miguel Island ERW Research - Quick Start Guide

**Date:** January 21, 2026  
**Location:** São Miguel, Azores, Portugal (37.78°N, 25.50°W)  
**Full Framework:** See `SAO_MIGUEL_RESEARCH_FRAMEWORK.md`

---

## 🎯 RESEARCH QUESTION

**Can São Miguel Island's volcanic basalts support economically viable Enhanced Rock Weathering for carbon dioxide removal, integrated with local dairy agriculture?**

---

## 🌋 SÃO MIGUEL AT A GLANCE

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Island Area** | 744 km² | Largest in Azores |
| **Basalt Coverage** | ~70% (520 km²) | Young volcanic flows |
| **Climate** | Oceanic subtropical | Perfect for ERW |
| **Rainfall** | 2,500 mm/yr | High weathering rate |
| **Temperature** | 17.5°C mean annual | Moderate, year-round |
| **Population** | 140,000 | Carbon neutral opportunity |
| **Main Economy** | Dairy farming | ERW = co-benefits |

---

## 📊 CORE HYPOTHESIS

**São Miguel's young, olivine-rich basalts (MgO 7-9%, CaO 9-11%) weathering under optimal oceanic climate can sequester 0.30-0.35 tCO₂/tonne basalt over 10 years, providing:**
1. Island-scale CDR: 15,000-30,000 tCO₂/year
2. Agricultural co-benefits: soil pH correction, reduced lime imports
3. Economic opportunity: carbon credits + cost savings

---

## 🔬 REQUIRED ANALYSES

### Analysis 1: São Miguel Basalt Geochemistry ⏱️ 2 minutes

```bash
python3 case_studies/sao_miguel.py
```

**What it calculates:**
- Basalt resource assessment (accessible Mt)
- Annual CDR potential (tCO₂/year)
- Agricultural integration (pasture area)
- Emissions context (% of island emissions offset)

**Expected Results:**
- Accessible basalt: ~3,750 Mt
- Annual CDR (conservative): 15,000 tCO₂/year
- ERW contribution: 2-4% of island emissions

---

### Analysis 2: Weathering Kinetics (São Miguel Climate) ⏱️ 5 minutes

**São Miguel-Specific Parameters:**
- Temperature: 17.5°C (coastal average)
- Rainfall: 2,500 mm/yr (island average)
- Soil pH: 5.5 (acidic volcanic soils)
- Basalt composition: MgO 7.5%, CaO 10.0%

**Expected CO₂ Uptake:**
- 1 year: ~40-50 kg CO₂/tonne
- 5 years: ~180-200 kg CO₂/tonne
- 10 years: **300-350 kg CO₂/tonne** (0.30-0.35 tCO₂/tonne)

**Climate Advantage:**
- High rainfall (2,500 mm) → 1.29× weathering boost
- Moderate temperature (17.5°C) → 1.40× boost
- **Combined climate factor: ~1.8× faster than temperate regions**

---

### Analysis 3: Agricultural Integration Assessment ⏱️ 3 minutes

**São Miguel Agriculture:**
- Dairy pastures: 250 km² (33% of island)
- Suitable for ERW: 200 km² (20,000 ha)
- Application rate: 50 tonnes basalt/ha
- Rotation cycle: 5 years

**Annual Basalt Demand (Agriculture):**
- Area treated per year: 4,000 ha
- Basalt needed: 200,000 tonnes/year
- CDR from agriculture: 60,000 tCO₂/year (full deployment)

**Co-Benefits:**
1. Soil pH correction (current pH 5.0-5.5 → target 6.0-6.5)
2. Replace imported lime (€40-60/tonne savings)
3. Micronutrients (Ca, Mg, Fe) for pasture
4. Yield increase: 10-20% (literature estimates)

---

## 📈 KEY RESULTS TO REPORT

### São Miguel Basalt Properties

| Property | Value | Interpretation |
|----------|-------|----------------|
| **SiO₂** | 48.5% | Basaltic composition |
| **MgO** | 7.5% | Moderate olivine content |
| **CaO** | 10.0% | High calcium (good for ERW) |
| **MgO + CaO** | 17.5% | High reactive silicate |
| **WPI** | 0.361 | **EXCELLENT** for ERW |
| **Porosity** | 8% | Vesicular (good surface area) |
| **Age** | <500,000 years | Young = high reactivity |

### Island-Scale CDR Potential

| Scenario | Basalt (t/yr) | CDR (tCO₂/yr) | % Island Emissions | Years Supply |
|----------|---------------|---------------|--------------------|--------------|
| **Conservative** | 50,000 | 15,000 | 2.1% | 75,000 years |
| **Moderate** | 75,000 | 22,500 | 3.2% | 50,000 years |
| **Aggressive** | 100,000 | 30,000 | 4.3% | 37,500 years |

**Recommendation:** Start with **moderate scenario (75,000 t/yr)**

---

## 🚀 IMMEDIATE NEXT STEPS

### Step 1: Run São Miguel Resource Assessment (2 min)

```bash
cd /Users/aswin/Documents/GitHub/ERW---Volcanic-Islands
python3 case_studies/sao_miguel.py
```

**Output:**
```
SÃO MIGUEL ISLAND (AZORES) - ERW RESOURCE & CDR ASSESSMENT
===============================================================

📍 LOCATION
  Island: São Miguel, Azores
  Area: 744 km²

🪨 BASALT RESOURCE ASSESSMENT
  Accessible Resource: 3,750 Mt
  Total CDR Potential: 1,125 MtCO₂

📅 ANNUAL SCENARIOS
  CONSERVATIVE: 50,000 t/yr → 15,000 tCO₂/yr
  MODERATE: 75,000 t/yr → 22,500 tCO₂/yr

✓ São Miguel has excellent ERW potential!
```

---

### Step 2: Review Full Framework

Read: `SAO_MIGUEL_RESEARCH_FRAMEWORK.md` (comprehensive 20-page guide)

---

### Step 3: Create São Miguel-Specific Data File

```bash
# Create data file for your São Miguel measurements
touch data/sao_miguel_basalt_samples.csv
```

**Template:**
```csv
sample_id,location,lat,lon,SiO2,MgO,CaO,Fe2O3,Al2O3,porosity
SM001,Sete_Cidades,37.87,-25.79,48.2,7.8,10.2,12.1,15.9,7.5
SM002,Fogo,37.76,-25.47,48.8,7.2,9.8,11.8,16.2,8.2
SM003,Furnas,37.77,-25.32,49.1,6.9,9.5,11.5,16.5,9.1
```

---

## 📝 MANUSCRIPT OUTLINE (São Miguel Focus)

**Title:** *Enhanced Rock Weathering Potential of São Miguel Island (Azores): Integrating Volcanic Basalt Carbon Removal with Dairy Agriculture*

### Structure

1. **Abstract** (250 words)
   - Context: Island carbon neutrality goals
   - Gap: Underutilized volcanic basalt for ERW
   - Method: Geochemical + climate + agricultural assessment
   - Result: 0.30-0.35 tCO₂/t potential, 15,000-30,000 tCO₂/yr island CDR
   - Impact: Model for volcanic islands worldwide

2. **Introduction** (~1200 words)
   - CDR necessity for islands (vulnerable to climate change)
   - ERW as nature-based solution
   - São Miguel as case study (accessible, well-studied geology)
   - Agricultural integration opportunity

3. **Methods** (~1000 words)
   - São Miguel geology & climate
   - Basalt geochemistry (literature + new samples if available)
   - Weathering kinetics model (climate-corrected)
   - Resource assessment (GIS + field survey)
   - Agricultural integration analysis

4. **Results** (~1200 words)
   - São Miguel basalt characterization (WPI = 0.36, excellent)
   - Climate-corrected CO₂ uptake (0.30-0.35 tCO₂/t @ 10 yr)
   - Resource assessment (3,750 Mt accessible)
   - Agricultural deployment (200 km² suitable pasture)
   - Island-scale CDR potential (15,000-30,000 tCO₂/yr)

5. **Discussion** (~1500 words)
   - Why São Miguel is ideal: young basalt + optimal climate + agriculture
   - Comparison to other islands (Hawaii, Iceland, Canaries)
   - Economic feasibility (carbon credits + co-benefits)
   - Limitations (need field validation, pilot project)
   - Scalability (model for 100+ volcanic islands globally)

6. **Conclusions** (~300 words)
   - São Miguel demonstrates viability of island-scale ERW
   - Recommend pilot project (10-20 ha dairy farm)
   - Transferable to other volcanic islands
   - Contributes to island carbon neutrality goals

---

## 📍 FIGURES REQUIRED

### Figure 1: São Miguel Island Map
- Volcanic complexes (Sete Cidades, Fogo, Furnas)
- Basalt flow distribution
- Agricultural zones (dairy pastures)
- Proposed pilot sites
- Climate zones (rainfall gradient)

### Figure 2: Basalt Geochemistry
- Panel A: TAS diagram (São Miguel basalts)
- Panel B: MgO vs. CaO (reactive silicate content)
- Panel C: WPI bar chart (São Miguel vs. other islands)

### Figure 3: CO₂ Uptake Kinetics
- Panel A: Time-series (0-10 years) with São Miguel climate
- Panel B: Climate sensitivity (rainfall 1800-3200 mm, temp 13-18°C)
- Panel C: Comparison to temperate regions

### Figure 4: Agricultural Integration
- Panel A: Pasture suitability map
- Panel B: Annual CDR by deployment scenario
- Panel C: Co-benefits (soil pH, yield, economics)

---

## ⚠️ CRITICAL ASSUMPTIONS

### Defend These

1. **Basalt composition assumed from literature**
   - **Action:** Collect 5-10 field samples for XRF analysis
   - **Defense:** Literature values consistent across Azores studies

2. **30% weathering efficiency**
   - **Justification:** Conservative estimate from Beerling et al. (2020)
   - **Defense:** Azores climate may achieve 35-40% (high rainfall)

3. **No field validation yet**
   - **Action:** Propose 3-year pilot project
   - **Defense:** Model based on robust literature kinetics

4. **Economic feasibility assumed**
   - **Gap:** Need cost-benefit analysis
   - **Action:** Calculate in follow-up study

---

## 📚 SÃO MIGUEL-SPECIFIC REFERENCES

### Must Cite

1. **Guest et al. (1999)** - *J. Petrology* - São Miguel volcanic evolution
2. **Queiroz et al. (2015)** - *J. Volcanology* - Fogo eruption history
3. **Wallenstein et al. (2007)** - São Miguel volcanism overview
4. **Madeira et al. (2007)** - *Geoderma* - Azores volcanic soils
5. **Azevedo (1996)** - Climate of the Azores

### ERW General

6. **Beerling et al. (2020)** - *Nature* - Global ERW potential
7. **Gislason & Oelkers (2003)** - *Chemical Geology* - Basalt weathering
8. **Kantola et al. (2017)** - *PLOS ONE* - Agricultural ERW

---

## 🎯 SUCCESS CRITERIA

Your São Miguel ERW study will be publication-ready when:

- [ ] São Miguel basalt geochemistry characterized (literature + samples)
- [ ] Climate-corrected weathering model run
- [ ] Resource assessment complete (accessible Mt calculated)
- [ ] Agricultural integration quantified (suitable ha, CDR potential)
- [ ] Island-scale CDR scenarios modeled (conservative to aggressive)
- [ ] 4 publication-quality figures generated (300+ dpi)
- [ ] Manuscript drafted (~5,000-6,000 words)
- [ ] Co-benefits quantified (soil pH, economics, yield)
- [ ] Pilot project proposed (location, cost, timeline)

---

## 🚀 YOUR NEXT COMMAND

```bash
# Run São Miguel assessment
cd /Users/aswin/Documents/GitHub/ERW---Volcanic-Islands
python3 case_studies/sao_miguel.py
```

**Expected runtime:** 2 minutes  
**Output:** Complete island-scale ERW assessment

---

**You now have a laser-focused São Miguel ERW research framework with no unnecessary data!** 🌋

---

*Focused on São Miguel Island only*  
*All Madeira and other island references removed*  
*Last updated: January 21, 2026*
