import pandas as pd
import random
from faker import Faker

fake = Faker()

platforms = ['Facebook', 'Instagram', 'Google Ads', 'LinkedIn', 'YouTube']
campaign_types = ['Awareness', 'Lead Gen', 'Retargeting']
regions = ['North', 'South', 'East', 'West', 'Central']
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
genders = ['Male', 'Female', 'Other']
devices = ['Mobile', 'Desktop', 'Tablet']

data = []

for _ in range(2000):
    start_date = fake.date_between(start_date='-120d', end_date='-15d')
    end_date = fake.date_between(start_date=start_date, end_date='today')
    impressions = random.randint(50000, 300000)
    clicks = random.randint(1000, 20000)
    conversions = random.randint(200, 5000)
    cost = round(random.uniform(5000, 50000), 2)
    revenue = cost + round(random.uniform(2000, 30000), 2)

    # Derived metrics
    ctr = round((clicks / impressions) * 100, 2)
    cpc = round(cost / clicks, 2)
    conversion_rate = round((conversions / clicks) * 100, 2)
    roi = round(((revenue - cost) / cost) * 100, 2)
    bounce_rate = round(random.uniform(10, 80), 2)

    data.append([
        fake.uuid4(),  # Campaign ID
        random.choice(platforms),
        random.choice(campaign_types),
        random.choice(regions),
        random.choice(age_groups),
        random.choice(genders),
        random.choice(devices),
        start_date,
        end_date,
        impressions,
        clicks,
        conversions,
        cost,
        revenue,
        ctr,
        cpc,
        conversion_rate,
        bounce_rate,
        roi
    ])

# Column names
columns = [
    "Campaign_ID", "Platform", "Campaign_Type", "Region", "Audience_AgeGroup", "Gender", "Device_Type",
    "Start_Date", "End_Date", "Impressions", "Clicks", "Conversions", "Cost", "Revenue",
    "CTR", "CPC", "Conversion_Rate", "Bounce_Rate", "ROI"
]

df = pd.DataFrame(data, columns=columns)

# Save to Excel
df.to_excel("advanced_marketing_dataset.xlsx", index=False)

print("✅ File created: advanced_marketing_dataset.xlsx")
