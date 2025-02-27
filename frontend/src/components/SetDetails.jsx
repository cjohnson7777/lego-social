

export function Theme({ themeName, sets }){
    return (
        <div className='mb-10 mt-20'>
          <h1 className='text-2xl font-bold ml-100' >{themeName}</h1>
          <SetDetails sets={sets}/>
        </div>
    )
}

function SetDetails({ sets }) {

    return (
      <div className="bg-white">
        <div className="mx-auto  max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
          <div className="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8">
          {sets.map((p, index) => (
                <div key={index} className="group" id='const'>
                <img
                  alt='lego-set'
                  src={p.set_img_url}
                  className="aspect-square w-full rounded-lg bg-gray-200 object-cover group-hover:opacity-75 xl:aspect-7/8"
                />
                <p className="mt-1 text-md font-medium text-gray-900">{p.name}</p>
                <p className="mt-2 text-md text-gray-700">{p.num_parts} Pieces</p>
              </div>
          ))}
          </div>
        </div>
      </div>
    )
  }
  


