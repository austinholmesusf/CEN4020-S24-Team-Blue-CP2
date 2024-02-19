# User Controller
# Provides endpoints for interacting with user data
from flask import jsonify, request

from incollege.services import UserService


def configure_user_routes(app):

    @app.route('/user_search', methods=['POST'])
    def handle_user_search():
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        return jsonify({'message': UserService.find_users_by_name(first_name, last_name)})


    @app.route('/update_preferences', methods=['POST'])
    def handle_update_pref():
        try:
            data = request.get_json()
            preference_name = data.get('preference')
            on = data.get('toggle')
            user_id = data.get('user_id')

            # how to pass user_id??
            result = UserService.update_preferences(user_id, preference_name, on)
            
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)})
