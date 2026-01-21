#!/usr/bin/env python3
"""
Enhanced Rock Weathering (ERW) Viability Analysis Script
São Miguel Island, Azores

Analyzes real soil data to quantify ERW potential and generate visualizations.
"""

import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Tuple
import json

@dataclass
class SoilPlot:
    """Represents a single agricultural plot with soil analysis data."""
    plot_id: str
    ph: float
    organic_matter: float  # %
    exchangeable_ca: float  # cmol/kg
    exchangeable_mg: float  # cmol/kg
    exchangeable_k: float  # cmol/kg
    cec: float  # cmol/kg
    base_saturation: float  # %
    p_extractable: float  # mg/kg
    k_extractable: float  # mg/kg
    area_ha: float = 2.0  # hectares

    @property
    def mg_ca_ratio(self) -> float:
        """Calculate Mg/Ca ratio."""
        return self.exchangeable_mg / self.exchangeable_ca if self.exchangeable_ca > 0 else 0

    @property
    def mg_deficit(self) -> float:
        """Calculate Mg deficit from optimal range (1.5-2.5 cmol/kg)."""
        optimal_min = 1.5
        return max(0, optimal_min - self.exchangeable_mg)


class ERWViabilityAnalyzer:
    """Analyzes ERW viability based on soil chemistry, climate, and economic factors."""
    
    # Climate constants for São Miguel
    ANNUAL_RAINFALL_MM = 1750  # mm/year
    AVG_TEMPERATURE_C = 18  # °C
    HUMIDITY_PERCENT = 80  # %
    
    # Economic constants
    LIME_COST_PER_TON = 40  # EUR/ton
    BASALT_COST_PER_TON = 13  # EUR/ton
    CARBON_CREDIT_PRICE = 80  # EUR/tCO2
    
    # Weathering model parameters
    BASALT_MGO_CONTENT = 0.08  # 8% MgO typical for São Miguel basalt
    BASALT_CAO_CONTENT = 0.10  # 10% CaO
    WEATHERING_EFFICIENCY = 0.45  # 45% weathering over 10 years
    
    def __init__(self, plots: List[SoilPlot]):
        self.plots = plots
        self.results = {}
    
    def calculate_ph_score(self, ph: float) -> float:
        """
        Calculate pH viability score (0-30 points).
        
        Weathering rate ∝ 10^(7-pH)
        Optimal pH: 5.0-5.5 (score = 30)
        """
        if ph <= 5.2:
            return 30.0
        elif ph <= 5.5:
            return 29.0
        elif ph <= 5.8:
            return 27.0
        elif ph <= 6.0:
            return 25.0
        elif ph <= 6.5:
            return 20.0
        elif ph <= 7.0:
            return 15.0
        else:
            return 5.0
    
    def calculate_om_score(self, om_percent: float) -> float:
        """
        Calculate organic matter score (0-20 points).
        
        High OM enhances weathering through:
        - Organic acid production
        - Microbial activity
        - Increased soil CO2
        """
        if om_percent >= 12:
            return 20.0
        elif om_percent >= 10:
            return 18.0
        elif om_percent >= 8:
            return 15.0
        elif om_percent >= 6:
            return 12.0
        elif om_percent >= 4:
            return 8.0
        else:
            return 3.0
    
    def calculate_mg_deficit_score(self, deficit: float) -> float:
        """
        Calculate Mg deficit score (0-15 points).
        
        Higher deficit = greater farmer motivation for basalt.
        """
        if deficit >= 1.5:
            return 15.0
        elif deficit >= 1.2:
            return 13.0
        elif deficit >= 1.0:
            return 11.0
        elif deficit >= 0.8:
            return 9.0
        elif deficit >= 0.5:
            return 6.0
        else:
            return 2.0
    
    def calculate_cec_score(self, cec: float) -> float:
        """
        Calculate CEC score (0-10 points).
        
        Higher CEC = greater ion exchange capacity.
        """
        if cec >= 20:
            return 10.0
        elif cec >= 15:
            return 9.0
        elif cec >= 10:
            return 8.0
        elif cec >= 8:
            return 6.0
        else:
            return 3.0
    
    def calculate_climate_score(self) -> float:
        """
        Calculate climate score (0-25 points).
        
        Based on rainfall and temperature.
        """
        # Rainfall component (0-15 points)
        if self.ANNUAL_RAINFALL_MM >= 1500:
            rainfall_score = 15.0
        elif self.ANNUAL_RAINFALL_MM >= 1000:
            rainfall_score = 12.0
        elif self.ANNUAL_RAINFALL_MM >= 750:
            rainfall_score = 9.0
        else:
            rainfall_score = 5.0
        
        # Temperature component (0-10 points)
        if 15 <= self.AVG_TEMPERATURE_C <= 20:
            temp_score = 10.0
        elif 12 <= self.AVG_TEMPERATURE_C <= 23:
            temp_score = 8.0
        else:
            temp_score = 5.0
        
        return rainfall_score + temp_score
    
    def calculate_total_viability_score(self, plot: SoilPlot) -> Dict[str, float]:
        """Calculate comprehensive viability score for a plot."""
        ph_score = self.calculate_ph_score(plot.ph)
        om_score = self.calculate_om_score(plot.organic_matter)
        mg_score = self.calculate_mg_deficit_score(plot.mg_deficit)
        cec_score = self.calculate_cec_score(plot.cec)
        climate_score = self.calculate_climate_score()
        
        total_score = ph_score + om_score + mg_score + cec_score + climate_score
        
        return {
            'plot_id': plot.plot_id,
            'ph_score': ph_score,
            'om_score': om_score,
            'mg_score': mg_score,
            'cec_score': cec_score,
            'climate_score': climate_score,
            'total_score': total_score,
            'rating': self._get_rating(total_score)
        }
    
    @staticmethod
    def _get_rating(score: float) -> str:
        """Convert numerical score to star rating."""
        if score >= 90:
            return "⭐⭐⭐⭐⭐ EXCEPTIONAL"
        elif score >= 80:
            return "⭐⭐⭐⭐⭐ EXCELLENT"
        elif score >= 70:
            return "⭐⭐⭐⭐ VERY GOOD"
        elif score >= 60:
            return "⭐⭐⭐ GOOD"
        elif score >= 50:
            return "⭐⭐ MODERATE"
        else:
            return "⭐ MARGINAL"
    
    def calculate_weathering_rate_multiplier(self, plot: SoilPlot) -> float:
        """
        Calculate weathering rate multiplier based on pH and OM.
        
        Base rate (pH 7.0, 2% OM) = 1.0x
        """
        # pH effect (exponential relationship)
        ph_multiplier = 10 ** (7.0 - plot.ph) / 10 ** (7.0 - 7.0)
        
        # Organic matter effect (linear enhancement)
        om_multiplier = 1.0 + (plot.organic_matter - 2.0) * 0.15
        
        # Climate effect
        climate_multiplier = (self.ANNUAL_RAINFALL_MM / 1000) * 1.2
        
        return ph_multiplier * om_multiplier * climate_multiplier
    
    def calculate_co2_removal_lime_replacement(self, plot: SoilPlot) -> Dict[str, float]:
        """
        Calculate CO2 removal for lime replacement scenario (conservative).
        
        Application: 2,700 kg basalt/ha/yr
        """
        # Basalt application rate (kg/ha/yr)
        basalt_rate = 2700
        
        # Calculate weatherable Mg and Ca content
        mgo_weathered = basalt_rate * self.BASALT_MGO_CONTENT * self.WEATHERING_EFFICIENCY
        cao_weathered = basalt_rate * self.BASALT_CAO_CONTENT * self.WEATHERING_EFFICIENCY
        
        # Weathering rate multiplier
        rate_multiplier = self.calculate_weathering_rate_multiplier(plot)
        
        # CO2 sequestration stoichiometry
        # MgO + CO2 → MgCO3: 40 g MgO sequesters 44 g CO2
        # CaO + CO2 → CaCO3: 56 g CaO sequesters 44 g CO2
        co2_from_mg = mgo_weathered * (44 / 40) * rate_multiplier / 1000  # t CO2/ha/yr
        co2_from_ca = cao_weathered * (44 / 56) * rate_multiplier / 1000  # t CO2/ha/yr
        
        total_co2_per_ha_yr = co2_from_mg + co2_from_ca
        total_co2_10yr = total_co2_per_ha_yr * 10 * plot.area_ha
        
        return {
            'scenario': 'Lime Replacement',
            'basalt_rate_kg_ha_yr': basalt_rate,
            'weathering_multiplier': round(rate_multiplier, 2),
            'co2_t_ha_yr': round(total_co2_per_ha_yr, 2),
            'co2_t_10yr_total': round(total_co2_10yr, 1),
            'plot_area_ha': plot.area_ha
        }
    
    def calculate_co2_removal_full_erw(self, plot: SoilPlot) -> Dict[str, float]:
        """
        Calculate CO2 removal for full ERW implementation (aggressive).
        
        Application: 50 t basalt/ha (one-time, 10-year weathering)
        """
        # Basalt application rate (kg/ha one-time)
        basalt_rate = 50000
        
        # Calculate weatherable Mg and Ca content
        mgo_weathered = basalt_rate * self.BASALT_MGO_CONTENT * self.WEATHERING_EFFICIENCY
        cao_weathered = basalt_rate * self.BASALT_CAO_CONTENT * self.WEATHERING_EFFICIENCY
        
        # Weathering rate multiplier
        rate_multiplier = self.calculate_weathering_rate_multiplier(plot)
        
        # CO2 sequestration over 10 years (decay model)
        # Assume faster weathering in years 1-5, slower in years 6-10
        co2_from_mg = mgo_weathered * (44 / 40) * rate_multiplier / 1000
        co2_from_ca = cao_weathered * (44 / 56) * rate_multiplier / 1000
        
        total_co2_10yr = (co2_from_mg + co2_from_ca) * plot.area_ha
        avg_co2_per_yr = total_co2_10yr / 10
        
        return {
            'scenario': 'Full ERW',
            'basalt_rate_kg_ha_onetime': basalt_rate,
            'weathering_multiplier': round(rate_multiplier, 2),
            'co2_t_ha_10yr': round(total_co2_10yr / plot.area_ha, 1),
            'co2_t_ha_yr_avg': round(avg_co2_per_yr / plot.area_ha, 1),
            'co2_t_10yr_total': round(total_co2_10yr, 1),
            'plot_area_ha': plot.area_ha
        }
    
    def calculate_economics(self, plot: SoilPlot, scenario: str = 'lime_replacement') -> Dict[str, float]:
        """Calculate economic analysis for farmer adoption."""
        if scenario == 'lime_replacement':
            # Current practice: 3,000 kg lime/ha/yr
            lime_cost = 3000 / 1000 * self.LIME_COST_PER_TON
            
            # Alternative: 2,700 kg basalt/ha/yr
            basalt_cost = 2700 / 1000 * self.BASALT_COST_PER_TON
            
            # CO2 removal benefit
            co2_data = self.calculate_co2_removal_lime_replacement(plot)
            carbon_revenue = co2_data['co2_t_ha_yr'] * self.CARBON_CREDIT_PRICE
            
        else:  # full_erw
            # One-time application: 50 t/ha
            lime_cost = 0  # no lime needed
            basalt_cost = 50 * self.BASALT_COST_PER_TON
            
            # CO2 removal benefit (averaged over 10 years)
            co2_data = self.calculate_co2_removal_full_erw(plot)
            carbon_revenue = co2_data['co2_t_ha_yr_avg'] * self.CARBON_CREDIT_PRICE
        
        cost_savings = lime_cost - basalt_cost
        total_benefit = cost_savings + carbon_revenue
        
        return {
            'scenario': scenario,
            'lime_cost_eur_ha_yr': round(lime_cost, 2),
            'basalt_cost_eur_ha_yr': round(basalt_cost, 2) if scenario == 'lime_replacement' else round(basalt_cost / 10, 2),
            'cost_savings_eur_ha_yr': round(cost_savings, 2) if scenario == 'lime_replacement' else round(basalt_cost / 10, 2),
            'carbon_revenue_eur_ha_yr': round(carbon_revenue, 2),
            'total_benefit_eur_ha_yr': round(total_benefit, 2) if scenario == 'lime_replacement' else round(carbon_revenue - basalt_cost/10, 2),
            'roi_percent': round((total_benefit / basalt_cost * 100), 1) if scenario == 'full_erw' else round((total_benefit / (basalt_cost if basalt_cost > 0 else 1) * 100), 1)
        }
    
    def analyze_all_plots(self) -> pd.DataFrame:
        """Perform comprehensive analysis on all plots."""
        results = []
        
        for plot in self.plots:
            viability = self.calculate_total_viability_score(plot)
            co2_lime = self.calculate_co2_removal_lime_replacement(plot)
            co2_full = self.calculate_co2_removal_full_erw(plot)
            economics_lime = self.calculate_economics(plot, 'lime_replacement')
            economics_full = self.calculate_economics(plot, 'full_erw')
            
            result = {
                'Plot ID': plot.plot_id,
                'pH': plot.ph,
                'Organic Matter (%)': plot.organic_matter,
                'Mg (cmol/kg)': plot.exchangeable_mg,
                'Ca (cmol/kg)': plot.exchangeable_ca,
                'Mg/Ca Ratio': round(plot.mg_ca_ratio, 3),
                'Mg Deficit': round(plot.mg_deficit, 2),
                'CEC (cmol/kg)': plot.cec,
                'Viability Score': round(viability['total_score'], 1),
                'Rating': viability['rating'],
                'Weathering Multiplier': co2_lime['weathering_multiplier'],
                'CO₂ Lime Repl. (t/ha/yr)': co2_lime['co2_t_ha_yr'],
                'CO₂ Full ERW (t/ha/yr)': co2_full['co2_t_ha_yr_avg'],
                'Benefit Lime Repl. (€/ha/yr)': economics_lime['total_benefit_eur_ha_yr'],
                'Benefit Full ERW (€/ha/yr)': economics_full['total_benefit_eur_ha_yr'],
            }
            results.append(result)
        
        return pd.DataFrame(results)
    
    def generate_summary_statistics(self, df: pd.DataFrame) -> Dict:
        """Generate summary statistics for all plots."""
        return {
            'n_plots': len(df),
            'avg_ph': round(df['pH'].mean(), 2),
            'std_ph': round(df['pH'].std(), 2),
            'avg_om': round(df['Organic Matter (%)'].mean(), 1),
            'std_om': round(df['Organic Matter (%)'].std(), 1),
            'avg_mg_deficit': round(df['Mg Deficit'].mean(), 2),
            'avg_viability_score': round(df['Viability Score'].mean(), 1),
            'total_area_ha': sum(plot.area_ha for plot in self.plots),
            'total_co2_lime_replacement_t_yr': round(df['CO₂ Lime Repl. (t/ha/yr)'].sum() * 2, 1),  # Assuming 2 ha per plot
            'total_co2_full_erw_t_yr': round(df['CO₂ Full ERW (t/ha/yr)'].sum() * 2, 1),
            'total_economic_benefit_lime_eur_yr': round(df['Benefit Lime Repl. (€/ha/yr)'].sum() * 2, 0),
            'total_economic_benefit_full_eur_yr': round(df['Benefit Full ERW (€/ha/yr)'].sum() * 2, 0),
        }
    
    def export_results(self, output_path: str = 'viability_results.csv'):
        """Export analysis results to CSV."""
        df = self.analyze_all_plots()
        df.to_csv(output_path, index=False)
        print(f"✅ Results exported to {output_path}")
        return df


def load_sao_miguel_data() -> List[SoilPlot]:
    """Load São Miguel soil analysis data from Sanguinho area."""
    plots = [
        SoilPlot("J. Moleiro 1", 5.6, 10, 7.2, 0.6, 0.7, 14.4, 58, 45, 180, 2.0),
        SoilPlot("J. Moleiro 2", 5.7, 9, 9.1, 0.8, 0.9, 17.9, 60, 38, 210, 2.0),
        SoilPlot("J. Moleiro 3", 5.5, 11, 6.5, 0.7, 0.6, 13.5, 59, 52, 170, 2.0),
        SoilPlot("J. Moleiro 4", 5.5, 10, 10.3, 0.9, 1.0, 19.2, 64, 41, 240, 2.0),
        SoilPlot("J. Moleiro 5", 5.2, 8, 6.0, 0.5, 0.5, 12.0, 58, 60, 150, 2.0),
        SoilPlot("J. Moleiro 6", 5.2, 7, 5.8, 0.6, 0.5, 11.8, 59, 65, 145, 2.0),
        SoilPlot("J. Moleiro 7", 5.3, 12, 7.9, 0.7, 0.8, 16.4, 59, 48, 200, 2.0),
        SoilPlot("J. Moleiro 8", 5.4, 9, 8.4, 0.8, 0.8, 16.0, 63, 43, 195, 2.0),
        SoilPlot("J. Moleiro 9", 5.9, 8, 11.2, 0.9, 1.1, 20.2, 65, 35, 260, 2.0),
        SoilPlot("J. Moleiro 10", 5.7, 9, 8.7, 0.7, 0.9, 16.3, 62, 40, 215, 2.0),
        SoilPlot("J. Moleiro 11", 6.0, 6, 9.8, 1.0, 1.0, 18.8, 63, 33, 235, 2.0),
    ]
    return plots


def main():
    """Main analysis workflow."""
    print("=" * 80)
    print("🌋 ENHANCED ROCK WEATHERING VIABILITY ANALYSIS")
    print("São Miguel Island, Azores - Sanguinho Agricultural Area")
    print("=" * 80)
    print()
    
    # Load data
    print("📊 Loading São Miguel soil data...")
    plots = load_sao_miguel_data()
    print(f"✅ Loaded {len(plots)} plots")
    print()
    
    # Initialize analyzer
    analyzer = ERWViabilityAnalyzer(plots)
    
    # Analyze all plots
    print("🔬 Performing viability analysis...")
    results_df = analyzer.analyze_all_plots()
    print("✅ Analysis complete")
    print()
    
    # Display results
    print("=" * 80)
    print("VIABILITY SCORES BY PLOT")
    print("=" * 80)
    print(results_df[['Plot ID', 'pH', 'Organic Matter (%)', 'Viability Score', 'Rating']].to_string(index=False))
    print()
    
    print("=" * 80)
    print("CO₂ REMOVAL POTENTIAL")
    print("=" * 80)
    print(results_df[['Plot ID', 'Weathering Multiplier', 'CO₂ Lime Repl. (t/ha/yr)', 'CO₂ Full ERW (t/ha/yr)']].to_string(index=False))
    print()
    
    print("=" * 80)
    print("ECONOMIC ANALYSIS")
    print("=" * 80)
    print(results_df[['Plot ID', 'Benefit Lime Repl. (€/ha/yr)', 'Benefit Full ERW (€/ha/yr)']].to_string(index=False))
    print()
    
    # Summary statistics
    summary = analyzer.generate_summary_statistics(results_df)
    print("=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)
    print(f"Number of plots:                {summary['n_plots']}")
    print(f"Total area:                     {summary['total_area_ha']:.1f} ha")
    print(f"Average pH:                     {summary['avg_ph']} ± {summary['std_ph']}")
    print(f"Average organic matter:         {summary['avg_om']}% ± {summary['std_om']}%")
    print(f"Average Mg deficit:             {summary['avg_mg_deficit']} cmol/kg")
    print(f"Average viability score:        {summary['avg_viability_score']}/100")
    print()
    print(f"Total CO₂ (lime replacement):   {summary['total_co2_lime_replacement_t_yr']:.1f} t/yr")
    print(f"Total CO₂ (full ERW):           {summary['total_co2_full_erw_t_yr']:.1f} t/yr")
    print()
    print(f"Total benefit (lime repl.):     €{summary['total_economic_benefit_lime_eur_yr']:,.0f}/yr")
    print(f"Total benefit (full ERW):       €{summary['total_economic_benefit_full_eur_yr']:,.0f}/yr")
    print()
    
    # Overall assessment
    print("=" * 80)
    print("OVERALL ASSESSMENT")
    print("=" * 80)
    if summary['avg_viability_score'] >= 90:
        rating = "⭐⭐⭐⭐⭐ EXCEPTIONAL"
        conclusion = "These soils are OUTSTANDING candidates for ERW!"
    elif summary['avg_viability_score'] >= 80:
        rating = "⭐⭐⭐⭐⭐ EXCELLENT"
        conclusion = "These soils are EXCELLENT candidates for ERW."
    elif summary['avg_viability_score'] >= 70:
        rating = "⭐⭐⭐⭐ VERY GOOD"
        conclusion = "These soils are very good candidates for ERW."
    else:
        rating = "⭐⭐⭐ GOOD"
        conclusion = "These soils are suitable for ERW with monitoring."
    
    print(f"Overall Rating: {rating}")
    print(f"Conclusion: {conclusion}")
    print()
    
    # Export results
    output_file = "/Users/aswin/Documents/GitHub/ERW---Volcanic-Islands/data/sao_miguel_viability_results.csv"
    analyzer.export_results(output_file)
    print()
    print(f"📁 Detailed results saved to: {output_file}")
    print()
    
    # Top recommendations
    print("=" * 80)
    print("TOP 3 PRIORITY PLOTS FOR PILOT PROJECT")
    print("=" * 80)
    top3 = results_df.nlargest(3, 'Viability Score')
    for idx, row in top3.iterrows():
        print(f"{row['Plot ID']}:")
        print(f"  - Viability Score: {row['Viability Score']:.1f}/100 ({row['Rating']})")
        print(f"  - pH: {row['pH']} (weathering multiplier: {row['Weathering Multiplier']:.1f}x)")
        print(f"  - CO₂ removal (lime repl.): {row['CO₂ Lime Repl. (t/ha/yr)']} t/ha/yr")
        print(f"  - Economic benefit: €{row['Benefit Lime Repl. (€/ha/yr)']:.0f}/ha/yr")
        print()
    
    print("=" * 80)
    print("✅ ANALYSIS COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
