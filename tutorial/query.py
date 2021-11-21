from gql import gql

get_person_list = gql("""
query MyQuery {
  person {
    id
    name
    house {
      address
    }
  }
}
""")

add_person = gql("""
mutation MyMutation (
  $name: String,
  $age: Int,
  $address: String
) {
  insert_person_one(object: {
    age: $age,
    house: {data: {address: $address}},
    name: $name}) {
    id
  }
}
""")