// $Id: maxmin.h,v 1.2 2005-02-22 22:12:38 jwpeterson Exp $

// The libMesh Finite Element Library.
// Copyright (C) 2002-2005  Benjamin S. Kirk, John W. Peterson
  
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
  
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
  
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

#ifndef __maxmin_h__
#define __maxmin_h__

template <class T>
inline const T& max (const T& a, const T& b)
{
  return b>a?b:a;
}

template <class T>
inline T& max (T &a, T &b)
{
  return b>a?b:a;
}

template <class T>
inline const T& min (const T& a, const T& b)
{
  return b>a?a:b;
}

template <class T>
inline T& min (T &a, T &b)
{
  return b>a?a:b;
}

#endif __maxmin_h__
