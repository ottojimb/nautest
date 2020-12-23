def query_string_osm(location: str):
    return f"""<osm-script output="json">
  <query type="node">
    <has-kv k="name" v="{location}"/>
  </query>
  <union>
    <query type="node">
      <around radius="1500"/>
      <has-kv k="amenity" regv="restaurant"/>
    </query>
  </union>
  <print mode="body"/>
  <recurse type="down"/>
  <print mode="skeleton"/>
</osm-script>""".encode(
        "utf-8"
    )
