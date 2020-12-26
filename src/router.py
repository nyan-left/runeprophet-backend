import pandas as pd
from fbprophet import Prophet
import json


async def predict(event, context):
    df = pd.DataFrame(json.loads(event['body']))
    df.head()
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=10)
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    json = forecast.to_json(orient='records', date_format='iso')
    response = {
        "statusCode": 200,
        "body": json
    }
    return response
