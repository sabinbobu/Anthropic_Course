# Streaming Service Churn Analysis - Complete Results

## Overview
This analysis examined 500 streaming service customers to identify the major drivers of churn (customer cancellation). The overall churn rate is **38.6%** (193 customers).

## Key Files Generated
1. **churn_analysis_detailed.png** - Comprehensive 8-panel visualization dashboard
2. **churn_analysis_report.txt** - Detailed executive summary with recommendations

## Executive Summary: Top Churn Drivers

### 1. **Low Viewing Engagement** (Feature Importance: 0.270) ⚠️ CRITICAL
- Churned customers watch **20% less content** (66.6 vs 83.2 hours/month)
- Customers viewing <67 hours/month are at high risk
- **Impact**: Most important predictor of churn

### 2. **Short Session Duration** (Feature Importance: 0.164) ⚠️ HIGH
- Churned customers have **14.4% shorter sessions** (49.4 vs 57.8 minutes)
- Indicates lower content satisfaction and engagement
- Sessions <50 minutes signal risk

### 3. **Limited Content Exploration** (Feature Importance: 0.157) ⚠️ HIGH  
- Churned customers watch **18.1% fewer unique titles** (19.5 vs 23.7 titles)
- Limited discovery may indicate poor content fit
- Users exploring <20 titles/month are vulnerable

### 4. **High Customer Service Interactions** (Feature Importance: 0.129) ⚠️ HIGH
- Churned customers have **27.7% MORE support interactions** (3.18 vs 2.49 per year)
- 3+ interactions per year signals serious issues
- Churn rate increases dramatically: 1 interaction = 27.3%, 4 interactions = 56.7%, 6 interactions = 75%

### 5. **Low Binge-Watching Frequency** (Feature Importance: 0.106)
- Churned customers have **19.7% fewer binge sessions** (6.2 vs 7.7)
- Binge-watching indicates strong content engagement

## Additional Risk Factors

### Subscription Tier
- **Basic**: 43.5% churn rate (207 customers)
- **Standard**: 39.5% churn rate (210 customers)  
- **Premium**: 24.1% churn rate (83 customers)
- Premium tier has **1.8x lower churn** than Basic

### Content Genre Preferences
**High-Risk Genres** (>40% churn):
- Horror: 52.3%
- Thriller: 48.3%
- Action: 44.6%
- Romance: 41.8%

**Low-Risk Genres** (<35% churn):
- Documentary: 25.9%
- Comedy: 33.0%

## High-Risk Customer Segments

### Segment 1: Low Engagement + High CS Contacts
- **Size**: 181 customers (36.2% of base)
- **Churn Rate**: 50.8% (1.3x higher than average)
- **Criteria**: <67 viewing hours/month AND ≥3 CS interactions

### Segment 2: Basic Tier + Low Engagement  
- **Size**: 105 customers (21.0% of base)
- **Churn Rate**: 53.3% (1.4x higher than average)
- **Criteria**: Basic subscription AND <70 viewing hours/month

## Strategic Recommendations

### 1. Engagement Improvement (CRITICAL Priority)
- Implement personalized content recommendations for low-engagement users
- Create targeted campaigns highlighting new content in preferred genres
- Develop "binge-worthy" content collections
- Set up automated alerts for users below 67 hours/month

### 2. Customer Service Optimization (HIGH Priority)
- Analyze root causes of support tickets
- Implement proactive outreach after 2+ interactions
- Improve self-service resources
- Track resolution satisfaction scores

### 3. Premium Tier Migration (HIGH Priority)
- Offer upgrade promotions for at-risk Basic users
- Highlight Premium benefits (quality, devices, exclusive content)
- Create conversion pathways with trial periods

### 4. Content Strategy (MEDIUM Priority)
- Expand Documentary and Comedy libraries
- Cross-promote genres to diversify habits
- Survey Horror/Thriller fans for content gaps

### 5. Predictive Churn System (CRITICAL Priority)
- Weekly automated customer risk scoring
- Alerts for high-risk segments
- Targeted retention offers
- A/B test intervention strategies

## Expected Business Impact

**Current monthly churn cost**: $2,316 (assuming $12 avg LTV per customer)

**Potential savings with churn reduction:**
- 10% reduction → Save 19 customers/month → **$232/month**
- 20% reduction → Save 38 customers/month → **$463/month**
- 30% reduction → Save 57 customers/month → **$695/month**

## Methodology

### Data Analysis
- **Sample Size**: 500 customers
- **Features Analyzed**: 8 behavioral and demographic variables
- **Statistical Tests**: T-tests for significance (all p < 0.05)

### Machine Learning Model
- **Algorithm**: Random Forest Classifier (200 trees)
- **Training Accuracy**: 73.1%
- **Testing Accuracy**: 63.3%
- **Purpose**: Feature importance ranking and predictive insights

### Key Metrics
- Churn rate by segment
- Engagement differences (churned vs retained)
- Feature importance scores
- Statistical significance testing

---

**Report Generated**: March 2024  
**Analysis Type**: Predictive Churn Analytics  
**Recommendation**: Immediate action on high-risk segments
