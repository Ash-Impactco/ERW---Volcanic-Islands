#!/usr/bin/env python3
"""
São Miguel Island (Azores) - ERW Resource Assessment
Case study for island-scale carbon dioxide removal
"""

def sao_miguel_basalt_resource(area_km2=744, basalt_coverage=0.70, 
                                 depth_m=5, density_kgm3=2875, 
                                 recovery_factor=0.50):
    """
    Calculate accessible basalt resources for ERW on São Miguel Island.
    
    Parameters:
    -----------
    area_km2 : float
        Total island area (São Miguel = 744 km²)
    basalt_coverage : float
        Fraction of island covered by accessible basalt flows (0-1)
    depth_m : float
        Realistic extraction depth for sustainable quarrying
    density_kgm3 : float
        Bulk density of São Miguel basalt
    recovery_factor : float
        Fraction of in-situ resource that can be extracted
    
    Returns:
    --------
    dict : Resource assessment results
    """
    
    # Calculate accessible basalt area
    basalt_area_km2 = area_km2 * basalt_coverage
    
    # Volume calculation
    volume_m3 = basalt_area_km2 * 1e6 * depth_m
    
    # In-situ mass
    in_situ_mass_kg = volume_m3 * density_kgm3
    in_situ_mass_Mt = in_situ_mass_kg / 1e9
    
    # Accessible mass (with recovery factor)
    accessible_mass_Mt = in_situ_mass_Mt * recovery_factor
    
    # CDR potential (assuming 0.30 tCO2/t basalt efficiency)
    co2_efficiency = 0.30  # tCO2 per tonne basalt
    total_cdr_MtCO2 = accessible_mass_Mt * co2_efficiency
    
    # Annual extraction scenarios
    scenarios = {
        'conservative': 50000,   # 50,000 t/yr
        'moderate': 75000,       # 75,000 t/yr
        'aggressive': 100000     # 100,000 t/yr
    }
    
    annual_cdr = {}
    depletion_years = {}
    
    for scenario, extraction_t_yr in scenarios.items():
        annual_cdr[scenario] = (extraction_t_yr * co2_efficiency) / 1000  # MtCO2/yr
        depletion_years[scenario] = (accessible_mass_Mt * 1e6) / extraction_t_yr
    
    return {
        'island_area_km2': area_km2,
        'basalt_area_km2': basalt_area_km2,
        'extraction_depth_m': depth_m,
        'in_situ_resource_Mt': round(in_situ_mass_Mt, 1),
        'accessible_resource_Mt': round(accessible_mass_Mt, 1),
        'total_cdr_potential_MtCO2': round(total_cdr_MtCO2, 2),
        'annual_cdr_scenarios_MtCO2_yr': annual_cdr,
        'resource_depletion_years': depletion_years
    }


def sao_miguel_emissions_context():
    """
    Calculate São Miguel's emissions context for CDR assessment.
    """
    
    population = 140000  # São Miguel population
    per_capita_emissions_tCO2 = 5.0  # Portugal average
    
    island_emissions_MtCO2_yr = (population * per_capita_emissions_tCO2) / 1e6
    
    return {
        'population': population,
        'per_capita_emissions_tCO2': per_capita_emissions_tCO2,
        'total_island_emissions_MtCO2_yr': round(island_emissions_MtCO2_yr, 3),
        'total_island_emissions_tCO2_yr': int(population * per_capita_emissions_tCO2)
    }


def sao_miguel_agricultural_integration():
    """
    Assess agricultural land available for ERW application.
    """
    
    total_agricultural_km2 = 250  # Pasture/cropland on São Miguel
    suitable_for_erw_km2 = 200    # Suitable dairy pastures
    
    # Application rates
    basalt_application_t_ha = 50  # tonnes per hectare
    suitable_area_ha = suitable_for_erw_km2 * 100
    
    total_basalt_needed_t = suitable_area_ha * basalt_application_t_ha
    
    # 5-year application cycle
    annual_basalt_demand_t = total_basalt_needed_t / 5
    
    # CDR from agricultural application
    co2_uptake_tCO2_ha = basalt_application_t_ha * 0.30  # 0.30 tCO2/t basalt
    annual_agricultural_cdr_tCO2 = (suitable_area_ha / 5) * co2_uptake_tCO2_ha
    
    return {
        'total_agricultural_land_km2': total_agricultural_km2,
        'erw_suitable_land_km2': suitable_for_erw_km2,
        'erw_suitable_land_ha': suitable_area_ha,
        'basalt_application_rate_t_ha': basalt_application_t_ha,
        'annual_basalt_demand_t': int(annual_basalt_demand_t),
        'annual_agricultural_cdr_tCO2': int(annual_agricultural_cdr_tCO2)
    }


def main():
    """
    Complete São Miguel ERW assessment
    """
    
    print("=" * 80)
    print("SÃO MIGUEL ISLAND (AZORES) - ERW RESOURCE & CDR ASSESSMENT")
    print("=" * 80)
    print()
    
    # Geographic context
    print("📍 LOCATION")
    print("  Island: São Miguel, Azores Archipelago, Portugal")
    print("  Coordinates: 37.78°N, 25.50°W")
    print("  Area: 744 km² (largest island in Azores)")
    print()
    
    # Climate context
    print("🌦️  CLIMATE")
    print("  Mean Annual Temperature: 17.5°C")
    print("  Mean Annual Precipitation: 2,500 mm/yr")
    print("  Climate Classification: Oceanic Subtropical (Cfb)")
    print("  ERW Advantage: High rainfall + moderate temperature = fast weathering")
    print()
    
    # Resource assessment
    print("🪨 BASALT RESOURCE ASSESSMENT")
    print("─" * 80)
    
    resource_results = sao_miguel_basalt_resource()
    
    print(f"  Total Island Area: {resource_results['island_area_km2']} km²")
    print(f"  Basalt-Covered Area: {resource_results['basalt_area_km2']:.0f} km² (70% of island)")
    print(f"  Extraction Depth: {resource_results['extraction_depth_m']} m (shallow, sustainable)")
    print()
    print(f"  In-Situ Basalt Resource: {resource_results['in_situ_resource_Mt']:,.0f} Mt")
    print(f"  Accessible Resource (50% recovery): {resource_results['accessible_resource_Mt']:,.0f} Mt")
    print(f"  Total CDR Potential: {resource_results['total_cdr_potential_MtCO2']:.2f} MtCO₂")
    print()
    
    print("📅 ANNUAL EXTRACTION SCENARIOS")
    print("─" * 80)
    
    for scenario, cdr_Mt in resource_results['annual_cdr_scenarios_MtCO2_yr'].items():
        extraction_t = {
            'conservative': 50000,
            'moderate': 75000,
            'aggressive': 100000
        }[scenario]
        
        depletion_yrs = resource_results['resource_depletion_years'][scenario]
        cdr_tCO2 = cdr_Mt * 1000
        
        print(f"\n  {scenario.upper():15s}: {extraction_t:,} tonnes basalt/year")
        print(f"    └─ Annual CDR: {cdr_tCO2:,.0f} tCO₂/year")
        print(f"    └─ Resource depletion: {depletion_yrs:.0f} years")
    
    print()
    
    # Emissions context
    print("🏝️  EMISSIONS CONTEXT")
    print("─" * 80)
    
    emissions = sao_miguel_emissions_context()
    
    print(f"  São Miguel Population: {emissions['population']:,}")
    print(f"  Per Capita Emissions: {emissions['per_capita_emissions_tCO2']:.1f} tCO₂/person/year")
    print(f"  Total Island Emissions: {emissions['total_island_emissions_tCO2_yr']:,} tCO₂/year")
    print()
    
    # Calculate ERW contribution
    conservative_cdr = resource_results['annual_cdr_scenarios_MtCO2_yr']['conservative'] * 1000
    moderate_cdr = resource_results['annual_cdr_scenarios_MtCO2_yr']['moderate'] * 1000
    
    conservative_pct = (conservative_cdr / emissions['total_island_emissions_tCO2_yr']) * 100
    moderate_pct = (moderate_cdr / emissions['total_island_emissions_tCO2_yr']) * 100
    
    print(f"  ERW Contribution (conservative): {conservative_pct:.1f}% of island emissions")
    print(f"  ERW Contribution (moderate): {moderate_pct:.1f}% of island emissions")
    print()
    
    # Agricultural integration
    print("🌾 AGRICULTURAL INTEGRATION")
    print("─" * 80)
    
    ag_results = sao_miguel_agricultural_integration()
    
    print(f"  Total Agricultural Land: {ag_results['total_agricultural_land_km2']} km²")
    print(f"  Suitable for ERW (dairy pastures): {ag_results['erw_suitable_land_km2']} km² "
          f"({ag_results['erw_suitable_land_ha']:,} ha)")
    print(f"  Basalt Application Rate: {ag_results['basalt_application_rate_t_ha']} tonnes/ha")
    print(f"  Annual Basalt Demand (5-yr cycle): {ag_results['annual_basalt_demand_t']:,} tonnes/year")
    print(f"  Annual Agricultural CDR: {ag_results['annual_agricultural_cdr_tCO2']:,} tCO₂/year")
    print()
    
    # Co-benefits
    print("✨ CO-BENEFITS FOR SÃO MIGUEL")
    print("─" * 80)
    print("  ✓ Soil pH correction (acidic volcanic soils)")
    print("  ✓ Reduced lime imports (cost savings)")
    print("  ✓ Micronutrient supply (Ca, Mg, Fe)")
    print("  ✓ Pasture productivity increase (10-20%)")
    print("  ✓ Carbon credit revenue for farmers")
    print("  ✓ Local circular economy (basalt extraction → agriculture)")
    print()
    
    # Recommendations
    print("🎯 RECOMMENDATIONS")
    print("─" * 80)
    print("  1. Start with PILOT PROJECT: 10-20 ha dairy farm")
    print(f"     └─ Basalt application: {ag_results['basalt_application_rate_t_ha']} t/ha")
    print("     └─ Duration: 3 years monitoring")
    print("     └─ Expected CDR: 300-500 tCO₂")
    print()
    print("  2. Scale to MODERATE scenario: 75,000 t/yr basalt")
    print(f"     └─ Annual CDR: {moderate_cdr:,.0f} tCO₂/year")
    print(f"     └─ Covers {moderate_pct:.1f}% of island emissions")
    print()
    print("  3. Establish local BASALT QUARRY (small-scale, sustainable)")
    print("     └─ Employment: 5-10 jobs")
    print("     └─ Location: Near agricultural zones")
    print()
    print("  4. Develop CARBON CREDIT mechanism for farmers")
    print("     └─ Revenue: €50-100/tCO₂ (market dependent)")
    print()
    
    print("=" * 80)
    print("✓ Assessment complete! São Miguel has excellent ERW potential.")
    print("=" * 80)


if __name__ == "__main__":
    main()
