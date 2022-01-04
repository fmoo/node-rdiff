{
  "targets": [
    {
      "target_name": "rdiff",
      "sources": [
        "rdiff.cc"
      ],
      "library_dirs": [
        "<(module_root_dir)/../librsync/dist/lib",
      ],
      "libraries": [
        "rsync.lib",
      ],
      'defines': ['LIBRSYNC_STATIC_DEFINE'],
      "include_dirs" : [
        "<(module_root_dir)/../librsync/dist/include",
        "<!(node -e \"require('nan')\")"
      ],
    }
  ]
}
