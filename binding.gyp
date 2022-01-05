{
  "targets": [
    {
      "target_name": "rdiff",
      "sources": [
        "rdiff.cc"
      ],
      "library_dirs": [
        "<(module_root_dir)/../librsync/dist/lib",
        "<(module_root_dir)/../librsync/dist/lib64",
      ],
      "libraries": [
        "-lrsync",
      ],
      'defines': ['LIBRSYNC_STATIC_DEFINE'],
      "include_dirs" : [
        "<(module_root_dir)/../librsync/dist/include",
        "<!(node -e \"require('nan')\")"
      ],
    }
  ]
}
