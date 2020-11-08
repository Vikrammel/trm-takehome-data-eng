from flask import Flask, request
app = Flask(__name__)

default_page_size = 100

def validate_request(req):
    """
    Ensure necessary fields and field requirements in direct exposure request
    """
    address  = req.args.get('address', None)
    if not address:
        return "No address provided"
    start_date = req.args.get('start_date', '0001-01-01T00:00:00Z')
    end_date = req.args.get('end_date', '9999-12-31T23:59:59Z')
    flow_type = req.args.get('flow_type', 'both')
    limit = req.args.get('limit', 100)
    offset = req.args.get('offset', 0)
    return {
        "start_date": start_date,
        "end_date": end_date,
        "flow_type": flow_type,
        "limit": limit,
        "offset": offset
    }

@app.route('/address/exposure/direct',  methods=['GET'])
def address_exposure_direct():
    # validate request is valid
    validation_resp = validate_request(request)
    if type(validation_resp) is str:
        # construct err resp
        return {
            "errors": [validation_resp]
        }

    # TODO: query db for requested addr & top n

    sample_res = {
        "chain": "btc",
        "top_n": [
            { "counterparty": "1FGhgLbMzrUV5mgwX9nkEeqHbKbUK29nbQ", "inflows": "0", "outflows": "0.01733177", "both": "0.01733177", "rank": 1 },
            { "counterparty": "1Huro4zmi1kD1Ln4krTgJiXMYrAkEd4YSh", "inflows": "0.01733177", "outflows": "0", "both": "0.01733177" , "rank": 2 },
        ],
        "rank_order_flowtype": "outflow",
        "next_offset": 2,
        "page_size": validation_resp.get("limit", default_page_size)
    }

    return sample_res

if __name__ =="__main__":
    # TODO: connect to postgres and run migrations before starting to serve

    app.run(debug=True, host="0.0.0.0", port=5000)
