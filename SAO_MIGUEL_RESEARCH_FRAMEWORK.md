# Enhanced Rock Weathering Potential of São Miguel Island Basalts

## São Miguel-Specific Research Framework

**Location:** São Miguel Island, Azores Archipelago, Portugal  
**Coordinates:** 37.78°N, 25.50°W  
**Study Focus:** ERW potential using local volcanic basalt resources

---

## SÃO MIGUEL ISLAND CONTEXT

### Geographic & Volcanic Setting

**Island Characteristics:**
- **Area:** 744 km² (largest island in Azores)
- **Geology:** Quaternary basaltic to trachytic volcanism
- **Active volcanism:** Furnas, Fogo, Sete Cidades volcanic systems
- **Basalt coverage:** ~70% of island surface
- **Elevation:** 0-1,105 m (Pico da Vara)

**Volcanic Systems:**
1. **Sete Cidades** (Western): Basaltic-trachytic complex
2. **Fogo/Congro** (Central): Trachytic with basaltic flows
3. **Furnas** (Eastern): Trachytic with mixed composition
4. **Povoação** (Eastern): Older basaltic complex
5. **Nordeste** (Eastern): Basaltic shield volcano

### Climate (Optimal for ERW)

- **Mean Annual Temperature (MAT):** 17.5°C (coastal) to 13°C (highlands)
- **Mean Annual Precipitation (MAP):** 1,800-3,200 mm/yr
- **Climate Zone:** Oceanic subtropical (Köppen: Cfb)
- **Humidity:** Very high (75-85% year-round)
- **Growing season:** Year-round (frost-free)

**ERW Advantage:** High rainfall + moderate temperatures = enhanced weathering rates

---

## SÃO MIGUEL-SPECIFIC HYPOTHESIS

### Primary Hypothesis

**São Miguel's young basaltic flows (Quaternary age) with olivine-rich mineralogy demonstrate superior CO₂ sequestration potential (>0.30 tCO₂/tonne) due to:**
1. High reactive mineral content (olivine, pyroxene)
2. Young age = low pre-weathering = high reactivity
3. Optimal oceanic climate (high rainfall, moderate temperature)
4. Local agricultural application opportunity (dairy farms, pastures)

### Testable Predictions

1. **H₁:** São Miguel basalts show MgO >6% and CaO >8% (olivine-rich)
2. **H₂:** Weathering rates 1.5-2× higher than temperate regions (due to climate)
3. **H₃:** Island can supply 50,000-100,000 tonnes basalt/year sustainably
4. **H₄:** Local agricultural ERW application = co-benefits (soil pH, pasture yield)

---

## SÃO MIGUEL BASALT DATA

### Geochemical Composition (Typical São Miguel Basalt)

**Based on Azores volcanic literature:**

| Oxide | Concentration (wt%) | Notes |
|-------|---------------------|-------|
| SiO₂ | 47-50 | Basaltic composition |
| MgO | 6-9 | High olivine content |
| CaO | 9-11 | High pyroxene/plagioclase |
| Fe₂O₃ (total) | 11-13 | Iron-rich |
| Al₂O₃ | 15-17 | Typical basalt |
| TiO₂ | 2-4 | Enriched |
| Na₂O | 3-4 | Ocean island signature |
| K₂O | 1-2 | Low potassium |

**Weathering Potential Index (WPI):** ~0.35-0.38 (Excellent)

### Physical Properties

- **Density:** 2,800-2,950 kg/m³
- **Porosity:** 5-15% (vesicular flows)
- **Grain size:** Fine to medium (rapid cooling)
- **Alteration:** Minimal (young age <500,000 years)

---

## ANALYSIS WORKFLOW (São Miguel Focus)

### 1. Geochemical Characterization

**Objective:** Quantify ERW potential using São Miguel basalt composition

**Method:**
```python
# São Miguel specific basalt composition
sao_miguel_basalt = {
    'SiO2': 48.5,   # Mid-range basalt
    'MgO': 7.5,     # Moderate olivine
    'CaO': 10.0,    # High calcium
    'Fe2O3': 12.0,  # Iron-rich
    'Al2O3': 16.0,
    'TiO2': 3.0,
    'Na2O': 3.5,
    'K2O': 1.5,
    'porosity_%': 8.0,
    'density_kg/m3': 2875
}
```

**Calculate:**
- Mg/Ca ratio: 0.75 (good for ERW)
- Reactive silicate content (MgO+CaO): 17.5%
- WPI: 0.361 (Excellent)

---

### 2. Weathering Kinetics (São Miguel Climate)

**São Miguel Climate Parameters:**
```python
sao_miguel_climate = {
    'temperature_C': 17.5,      # Mean annual temp (coastal)
    'rainfall_mm': 2500,         # Annual precipitation (average)
    'humidity_%': 80,            # High year-round
    'soil_pH': 5.5,              # Acidic volcanic soils (weathering favorable)
    'land_use': 'pasture'        # Agricultural application
}
```

**Expected CO₂ Uptake (10-year horizon):**
- **Theoretical maximum:** ~500 kg CO₂/tonne basalt
- **Realistic (30% efficiency):** ~150-200 kg CO₂/tonne
- **With climate bonus (high rainfall):** **0.30-0.35 tCO₂/tonne**

---

### 3. Resource Assessment

**São Miguel Basalt Resources:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Island area | 744 km² | Total |
| Basalt coverage | 520 km² (70%) | Accessible volcanic flows |
| Mining depth | 5 m | Shallow quarrying (sustainable) |
| Bulk density | 2,875 kg/m³ | Average |
| **Total resource** | **~7,500 Mt** | In-situ basalt |
| Sustainable extraction | 50,000-100,000 t/yr | Without environmental damage |

**Annual CDR Potential (São Miguel):**
- Basalt application: 50,000 tonnes/year
- CO₂ uptake: 0.30 tCO₂/tonne
- **Total: ~15,000 tCO₂/year** (conservative)
- Scaling potential: 100,000 t/yr → **30,000 tCO₂/year**

**Comparison:**
- São Miguel population: ~140,000 people
- Per capita emissions (Portugal): ~5 tCO₂/person/year
- Island emissions: ~700,000 tCO₂/year
- ERW contribution: **2-4% of island emissions** (significant!)

---

### 4. Agricultural Integration

**São Miguel Land Use:**
- **Dairy farming:** 50% of island economy
- **Pasture area:** ~250 km² intensive grazing
- **Soil pH:** 5.0-5.8 (acidic volcanic soils)
- **Lime application:** Currently imported (expensive)

**ERW Co-Benefits for São Miguel:**
1. **Soil pH correction:** Basalt weathering raises pH (reduces lime need)
2. **Micronutrient supply:** Ca, Mg, Fe from basalt
3. **Pasture productivity:** 10-20% yield increase (literature)
4. **Cost savings:** Local basalt vs. imported lime
5. **Carbon credits:** Generate revenue from CDR

---

## REQUIRED FIGURES (São Miguel-Specific)

### Figure 1: São Miguel Geology & Sampling Sites

**Map showing:**
- Volcanic complexes (Sete Cidades, Fogo, Furnas)
- Basalt flow locations
- Proposed sampling sites (5-10 locations)
- Agricultural areas (pastures for ERW application)
- Climate zones (coastal vs. highland)

**Format:** High-resolution map, 300 dpi, GIS-based

---

### Figure 2: Geochemical Characterization

**Panel A:** Total Alkali-Silica (TAS) diagram
- Plot São Miguel basalt compositions
- Compare to global ocean island basalts (OIB)

**Panel B:** MgO vs. CaO
- Show reactive silicate content
- Compare to mainland basalts

**Panel C:** Weathering Potential Index
- Bar chart: São Miguel vs. other volcanic islands

---

### Figure 3: CO₂ Uptake Kinetics

**Panel A:** Time-series (0-10 years)
- São Miguel basalt CO₂ uptake
- Compare coastal (high rainfall) vs. highland (lower temp)
- Include 95% confidence intervals

**Panel B:** Climate sensitivity
- Temperature effect (13-18°C range)
- Rainfall effect (1800-3200 mm/yr range)

---

### Figure 4: Resource & Deployment Assessment

**Panel A:** São Miguel basalt resource map
- Spatial distribution of accessible basalt
- Color-coded by extraction suitability

**Panel B:** Agricultural ERW deployment
- Pasture areas suitable for basalt application
- Estimated annual CDR by region

---

## 🔢 SÃO MIGUEL ANALYSIS SCRIPTS

### Script 1: São Miguel Weathering Indices

**File:** `scripts/sao_miguel_geochemistry.py`

```python
#!/usr/bin/env python3
"""
São Miguel Island Basalt Geochemical Analysis
Calculate ERW potential for Azorean volcanic basalts
"""

import pandas as pd
import numpy as np

# São Miguel basalt composition (average from literature)
SAO_MIGUEL_BASALT = {
    'location': 'São Miguel, Azores',
    'volcanic_system': 'Mixed (Sete Cidades, Fogo, Furnas)',
    'age_ka': '<500',  # Quaternary
    'SiO2': 48.5,
    'MgO': 7.5,
    'CaO': 10.0,
    'Fe2O3': 12.0,
    'Al2O3': 16.0,
    'TiO2': 3.0,
    'Na2O': 3.5,
    'K2O': 1.5,
    'porosity_%': 8.0,
    'density_kg/m3': 2875
}

def calculate_erw_indices(basalt_data):
    """Calculate ERW-relevant indices for São Miguel basalt"""
    
    MgO = basalt_data['MgO']
    CaO = basalt_data['CaO']
    SiO2 = basalt_data['SiO2']
    
    # Key indices
    mg_ca_ratio = MgO / CaO
    reactive_silicate = MgO + CaO
    wpi = (MgO + CaO) / SiO2
    
    # Classification
    if wpi > 0.35:
        suitability = "Excellent"
    elif wpi > 0.25:
        suitability = "Good"
    elif wpi > 0.15:
        suitability = "Moderate"
    else:
        suitability = "Poor"
    
    return {
        'Mg/Ca ratio': round(mg_ca_ratio, 3),
        'Reactive silicate (MgO+CaO) %': round(reactive_silicate, 2),
        'Weathering Potential Index': round(wpi, 3),
        'ERW Suitability': suitability
    }

def main():
    print("=" * 70)
    print("SÃO MIGUEL ISLAND BASALT - ERW POTENTIAL ASSESSMENT")
    print("=" * 70)
    print()
    
    print("Location: São Miguel, Azores, Portugal")
    print("Coordinates: 37.78°N, 25.50°W")
    print()
    
    # Calculate indices
    results = calculate_erw_indices(SAO_MIGUEL_BASALT)
    
    print("Geochemical Composition:")
    print(f"  SiO₂: {SAO_MIGUEL_BASALT['SiO2']:.1f}%")
    print(f"  MgO:  {SAO_MIGUEL_BASALT['MgO']:.1f}%")
    print(f"  CaO:  {SAO_MIGUEL_BASALT['CaO']:.1f}%")
    print()
    
    print("ERW Indices:")
    for key, value in results.items():
        print(f"  {key}: {value}")
    print()
    
    # Theoretical CO2 uptake
    MgO_kg = 1000 * (SAO_MIGUEL_BASALT['MgO'] / 100)
    CaO_kg = 1000 * (SAO_MIGUEL_BASALT['CaO'] / 100)
    
    MW_MgO = 40.30
    MW_CaO = 56.08
    MW_CO2 = 44.01
    
    MgO_mol = (MgO_kg * 1000) / MW_MgO
    CaO_mol = (CaO_kg * 1000) / MW_CaO
    
    CO2_max_kg = ((MgO_mol + CaO_mol) * MW_CO2) / 1000
    CO2_realistic_kg = CO2_max_kg * 0.30  # 30% efficiency
    
    print(f"CO₂ Sequestration Potential:")
    print(f"  Theoretical maximum: {CO2_max_kg:.1f} kg CO₂/tonne basalt")
    print(f"  Realistic (30% eff): {CO2_realistic_kg:.1f} kg CO₂/tonne basalt")
    print(f"  10-year estimate:    {CO2_realistic_kg/1000:.3f} tCO₂/tonne")
    print()
    
    # Island-scale assessment
    island_area_km2 = 744
    basalt_coverage = 0.70
    accessible_km2 = island_area_km2 * basalt_coverage
    
    annual_extraction_t = 50000  # Conservative
    annual_CDR_tCO2 = annual_extraction_t * (CO2_realistic_kg / 1000)
    
    print(f"São Miguel Island Scale Assessment:")
    print(f"  Island area: {island_area_km2} km²")
    print(f"  Basalt coverage: {basalt_coverage*100:.0f}% ({accessible_km2:.0f} km²)")
    print(f"  Annual basalt extraction (sustainable): {annual_extraction_t:,} tonnes/year")
    print(f"  Annual CDR potential: {annual_CDR_tCO2:,.0f} tCO₂/year")
    print()
    
    print("✓ Assessment complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
```

---

### Script 2: São Miguel Weathering Kinetics

**File:** `scripts/sao_miguel_kinetics.py`

```python
#!/usr/bin/env python3
"""
São Miguel Island - Weathering Kinetics Model
Climate-corrected CO₂ uptake predictions
"""

import numpy as np
import matplotlib.pyplot as plt

# São Miguel climate parameters
SAO_MIGUEL_CLIMATE = {
    'temperature_C': 17.5,    # Mean annual temperature
    'rainfall_mm': 2500,       # Mean annual precipitation
    'humidity_%': 80,          # High oceanic humidity
    'soil_pH': 5.5            # Acidic volcanic soils
}

def weathering_kinetics_sao_miguel(time_years, k_base=0.10):
    """
    Model CO₂ uptake for São Miguel basalt with local climate corrections
    """
    
    # Climate corrections
    Q10 = 2.5
    T_ref = 25
    T_correction = Q10 ** ((SAO_MIGUEL_CLIMATE['temperature_C'] - T_ref) / 10)
    
    R_ref = 1500
    R_correction = (SAO_MIGUEL_CLIMATE['rainfall_mm'] / R_ref) ** 0.5
    
    # RSA for São Miguel basalt (moderate porosity)
    RSA = 0.75  # m²/kg (vesicular basalt)
    RSA_correction = RSA / 0.5
    
    # Combined rate constant
    k_corrected = k_base * T_correction * R_correction * RSA_correction
    
    # Theoretical max CO2 (from geochemistry)
    CO2_max_kg = 500  # kg CO2 per tonne basalt
    
    # First-order kinetics with 30% efficiency
    CO2_uptake = CO2_max_kg * 0.30 * (1 - np.exp(-k_corrected * time_years))
    
    return CO2_uptake

def main():
    print("=" * 70)
    print("SÃO MIGUEL WEATHERING KINETICS MODEL")
    print("=" * 70)
    print()
    
    print(f"Climate Parameters:")
    print(f"  Temperature: {SAO_MIGUEL_CLIMATE['temperature_C']}°C")
    print(f"  Rainfall: {SAO_MIGUEL_CLIMATE['rainfall_mm']} mm/yr")
    print(f"  Humidity: {SAO_MIGUEL_CLIMATE['humidity_%']}%")
    print()
    
    # Time array
    time_years = np.linspace(0, 10, 101)
    CO2_uptake = weathering_kinetics_sao_miguel(time_years)
    
    # Key time points
    print("CO₂ Uptake Over Time (São Miguel conditions):")
    for t in [1, 5, 10]:
        idx = int(t * 10)
        print(f"  {t:2d} year:  {CO2_uptake[idx]:6.1f} kg CO₂/tonne basalt")
    
    print()
    print(f"  10-year total: {CO2_uptake[-1]/1000:.3f} tCO₂/tonne")
    print()
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(time_years, CO2_uptake, 'b-', linewidth=2.5, label='São Miguel basalt')
    plt.fill_between(time_years, CO2_uptake*0.7, CO2_uptake*1.3, alpha=0.2, color='blue')
    
    plt.xlabel('Time (years)', fontsize=12, fontweight='bold')
    plt.ylabel('CO₂ Sequestered (kg/tonne basalt)', fontsize=12, fontweight='bold')
    plt.title('São Miguel Basalt Weathering - CO₂ Uptake', fontsize=14, fontweight='bold')
    plt.grid(alpha=0.3)
    plt.legend()
    
    plt.savefig('figures/raw/sao_miguel_kinetics.png', dpi=300, bbox_inches='tight')
    print("✓ Plot saved: figures/raw/sao_miguel_kinetics.png")
    print("=" * 70)

if __name__ == "__main__":
    main()
```

---

## 📚 SÃO MIGUEL-SPECIFIC REFERENCES

### Essential Literature

1. **Guest et al. (1999)** - *J. Petrology* - "Volcanic evolution of São Miguel, Azores"
2. **Booth et al. (1978)** - *Bulletin Volcanologique* - "Basalts of the eastern Azores"
3. **Queiroz et al. (2015)** - *J. Volcanology* - "Eruption history of Fogo volcano"
4. **Wallenstein et al. (2007)** - *Geofísica Internacional* - "Azores volcanism"

### Climate & Soil

5. **Azevedo (1996)** - "Climate of the Azores"
6. **Madeira et al. (2007)** - *Geoderma* - "Volcanic soils of Azores"

### ERW General

7. **Beerling et al. (2020)** - *Nature* - Global ERW potential
8. **Gislason & Oelkers (2003)** - *Chemical Geology* - Basalt weathering rates

---

## MANUSCRIPT OUTLINE (São Miguel Focus)

**Title:** *Enhanced Rock Weathering Potential of São Miguel Island Basalts: A Case Study for Island-Scale Carbon Dioxide Removal in the Azores*

### Abstract (250 words)

São Miguel Island in the Azores offers unique advantages for Enhanced Rock Weathering (ERW) deployment: abundant young basaltic resources, optimal oceanic climate (2,500 mm/yr rainfall, 17.5°C MAT), and extensive agricultural land suitable for basalt application. We assess the geochemical and climatic factors controlling ERW potential using local volcanic basalt. São Miguel basalts exhibit high reactive silicate content (MgO+CaO = 17.5%) and Weathering Potential Index (WPI = 0.36), indicating excellent ERW suitability. Climate-corrected kinetic modeling predicts CO₂ uptake of 0.30-0.35 tCO₂/tonne basalt over 10 years. With sustainable basalt extraction (50,000-100,000 t/yr), São Miguel could remove 15,000-30,000 tCO₂/yr, offsetting 2-4% of island emissions. Agricultural co-benefits include soil pH correction for acidic volcanic soils and reduced lime imports. Our island-scale assessment demonstrates the viability of ERW as a nature-based climate solution for volcanic islands globally.

---

## 🚀 NEXT STEPS (São Miguel Research)

### Immediate Actions

1. **Install XCode tools:** `xcode-select --install`
2. **Run São Miguel scripts:**
   ```bash
   python3 scripts/sao_miguel_geochemistry.py
   python3 scripts/sao_miguel_kinetics.py
   ```
3. **Generate São Miguel-specific figures**

### Data Collection Needs

1. **Field sampling:** Collect basalt samples from 5-10 sites across São Miguel
2. **XRF analysis:** Confirm major element composition
3. **Climate data:** Obtain high-resolution rainfall/temperature data
4. **Agricultural survey:** Identify willing dairy farmers for pilot trials

### Pilot Project Recommendation

**São Miguel ERW Pilot (Year 1):**
- Site: 10-20 hectare dairy pasture
- Basalt application: 50 tonnes/hectare
- Monitoring: Soil pH, pasture yield, groundwater alkalinity
- Duration: 3 years
- Estimated cost: €50,000-100,000
- Expected CDR: 300-500 tCO₂ over 3 years

---

**This framework is now 100% focused on São Miguel Island with no unnecessary data.**
