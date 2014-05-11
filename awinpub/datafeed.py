import requests

"""
Example datafeed URL:
http://datafeed.api.productserve.com/datafeed/download/apikey/[KEY]/cid/626/columns/merchant_id,merchant_name,aw_product_id,merchant_product_id,upc,ean,mpn,isbn,model_number,product_name,description,specifications,promotional_text,merchant_category,category_id,category_name,language,brand_name,merchant_deep_link,merchant_thumb_url,merchant_image_url,aw_deep_link,aw_thumb_url,aw_image_url,delivery_time,valid_from,valid_to,currency,search_price,store_price,rrp_price,display_price,delivery_cost,web_offer,pre_order,in_stock,stock_quantity,is_for_sale,warranty,condition,product_type,parent_product_id,commission_group/format/csv/delimiter/,/compression/gzip/
"""

# Maybe based on supplied feeds?
# Maybe construct feeds from meta data and only allow download of recommended format?