import os
os.environ[ 'MPLCONFIGDIR' ] = '/tmp/'

if os.environ.get("AWS_EXECUTION_ENV") is not None:
  try:
    import unzip_requirements
  except ImportError:
    pass
  
import pandas as pd
from fbprophet import Prophet
import json

def predict(event, context):
  data = json.loads(event['body'])
  df = pd.DataFrame(data)
  df.head()
  m = Prophet()
  m.fit(df)
  future = m.make_future_dataframe(periods=30)
  future.tail()
  forecast = m.predict(future)
  forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
  jsonResponse = forecast.to_json(orient='records', date_format='iso')
  response = {
      "statusCode": 200,
      "body": jsonResponse
  }
  return response
