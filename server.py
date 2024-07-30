from flask import Flask, render_template, request
import os
import calc as c
from dotenv import load_dotenv
from azure.cosmos import CosmosClient, PartitionKey, exceptions

app = Flask(__name__)

# Load env variables from .env file
load_dotenv()

print (os.environ['COSMOS_ENDPOINT'])


#Azure Cosmos DB config
COSMOS_ENDPOINT = os.environ['COSMOS_ENDPOINT']
COSMOS_KEY = os.environ['COSMOS_KEY']
DATABASE_NAME = 'ResultsDB'
CONTAINER_NAME = 'ResultsContainer'

#Init the Cosmos client
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.create_database_if_not_exists(id=DATABASE_NAME)
container = database.create_container_if_not_exists(
    id = CONTAINER_NAME,
    partition_key = PartitionKey(path="/id"),
    offer_throughput=400
)


@app.route('/')
def hello():
    return 'Flask pythonserver', 200, {'Content-Type': 'text/plain'}

@app.route('/links')
def links():
    return render_template('index.html')

@app.route('/calculator')
def calculator():
    return render_template('calc.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    result = c.add(number1, number2)  # Assuming you have an add function in calc module

    # Store result in C DB
    result_item ={
        'id': str(number1) + '_' + str(number2),
        'result': result
    }

    container.upsert_item(result_item)

    return f'The result is {result}', 200, {'Content-Type': 'text/plain'}



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.logger.info(f'Server running on port {port}')
    app.run(host='0.0.0.0', port=port)