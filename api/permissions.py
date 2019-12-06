from rest_framework.permissions import BasePermission

class IsStaffOrOrderOwner(BasePermission):
	message = "You must be the owner of this order"

	def has_object_permission(self, request, view, object):
		if request.user.is_staff or (object.profile.user == request.user):
			return True
		else:
			return False
