import casbin_sqlalchemy_adapter
import casbin

adapter = casbin_sqlalchemy_adapter.Adapter("postgresql://postgres:postgres@db:5432/db")

e = casbin.Enforcer("casbin_example/model.conf", adapter)



# e.add_policy(
#     "fff", "data1", "read"
# )

e.add_policy("reader", "client", "read")
e.add_policies([("author", "client", "modify"), ("author", "client", "share"), ("admin", "client", "delete")])

e.add_grouping_policy("bob", "reader")


print(e.get_permissions_for_user("reader"))
# emmm.. mabe we can wrap this function....so it is with created by and created at..

sub = "bob"  # the user that wants to access a resource.
obj = "client"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.
if e.enforce(sub, obj, act):
    # permit alice to read data1casbin_sqlalchemy_adapter
    print("pass")
    pass
else:
    # deny the request, show an error
    print("deny")
    pass
