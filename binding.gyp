{
  "targets": [
    {
      "target_name": "rdiff",
      "sources": [
        "rdiff.cc"
      ],
      "libraries": [
        "<(module_root_dir)/../librsync/librsync.a",
        "-lz"
      ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ],
    }
  ]
}
